from .models import QueryData
import os
import shutil
from datetime import timedelta
from django.utils import timezone
from .models import ResourceCleanupLog


def cleanup_task(stdout,style,expiration_minutes=1,):
    
    stdout.write(style.WARNING("\n[INFO] Cleanup process started."))
    expiration_time = timezone.now() - timedelta(minutes=expiration_minutes)
    expired_data = QueryData.objects.filter(timestamp__lt=expiration_time)
    stdout.write(style.WARNING(f"[INFO] Found {expired_data.count()} expired record(s)."))

    for data in expired_data:
        if data.query_file and os.path.exists(data.query_file.path):
            file_name = os.path.basename(data.query_file.name)
            uploaded_at = data.timestamp
            data.query_file.delete(save=False)          # Delete the actual file from server's filesystem

            ResourceCleanupLog.objects.create(
            file_name=file_name,
            uploaded_at=uploaded_at,
            session_id=None,
            )
            stdout.write(style.NOTICE(f"[DEBUG] Deleted file: {file_name}"))
            file_name, uploaded_at = None, None
        
        data.delete()                                   # Delete record from DB (path reference)        
    

    stdout.write(style.SUCCESS("[DONE] File cleanup completed."))

    stdout.write(style.WARNING("\n[INFO] Starting Chroma DB cleanup."))
    try:
        chroma_db_path = 'media/NLP_data/chroma_db'
        if os.path.exists(chroma_db_path):
            shutil.rmtree(chroma_db_path)
            stdout.write(style.SUCCESS("[INFO] Chroma DB directory cleared."))
        else:
            stdout.write(style.WARNING(f"[WARN] Chroma DB path '{chroma_db_path}' does not exist."))
    except Exception as e:
        stdout.write(style.ERROR(f"[ERROR] Failed to clear Chroma DB: {e}"))

    stdout.write(style.SUCCESS("[DONE] Cleanup process completed.\n"))
