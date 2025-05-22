from .models import QueryData
import os
import shutil
from datetime import timedelta
from django.utils import timezone
from celery import shared_task
from langchain_chroma import Chroma


@shared_task
def cleanup_task(expiration_minutes=1):
    print("\n[INFO] Cleanup process started.")
    expiration_time = timezone.now() - timedelta(minutes=expiration_minutes)
    expired_data = QueryData.objects.filter(timestamp__lt=expiration_time)
    print(f"[INFO] Found {expired_data.count()} expired record(s).")

    for data in expired_data:
        if data.query_file and os.path.exists(data.query_file.path):
            print(f"[DEBUG] Deleted file: {data.query_file.name}")
            data.query_file.delete(save=False)
        data.delete()

    print("[INFO] File cleanup completed.")

    print("\n[INFO] Starting Chroma DB cleanup.")
    try:
        chroma_db_path = 'media/NLP_data/chroma_db'
        if os.path.exists(chroma_db_path):
            shutil.rmtree(chroma_db_path)
            print(f"[INFO] Chroma DB directory '{chroma_db_path}' cleared.")
        else:
            print(f"[WARN] Chroma DB path '{chroma_db_path}' does not exist.")
    except Exception as e:
        print(f"[ERROR] Failed to clear Chroma DB: {e}")

    print("[INFO] Cleanup process completed.\n")
