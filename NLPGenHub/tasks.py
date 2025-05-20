from .models import QueryData
import os
import shutil
from datetime import timedelta
from django.utils import timezone
from celery import shared_task

@shared_task
def cleanup_task(expiration_minutes=2):
    print("Cleanup started")
    expiration_time = timezone.now() - timedelta(minutes=expiration_minutes)
    expired_data = QueryData.objects.filter(timestamp__lt=expiration_time)

    for data in expired_data:
        if data.query_file and os.path.exists(data.query_file.path):
            os.remove(data.query_file.path)

        vector_db_path = 'media/NLP_data/chroma_db'
        if os.path.exists(vector_db_path):
            shutil.rmtree(vector_db_path)

        data.delete()

    print("Cleanup completed")
