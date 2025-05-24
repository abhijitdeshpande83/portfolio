import os
from django.db import models
from zoneinfo import ZoneInfo

# Create your models here.

class QueryData(models.Model):
    query_file = models.FileField(upload_to='NLP_data',blank=True, null=True)
    file_hash = models.CharField(max_length=255, unique=True, primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query_file.name
    
    def delete(self, *args, **kwargs):
        if self.query_file and os.path.isfile(self.query_file.path):
            os.remove(self.query_file.path)         # removes file from file system
        super().delete(*args, **kwargs)             # removes file reference path from DB

class ResourceCleanupLog(models.Model):
    file_name = models.CharField(max_length=255, null=True, blank=True)
    uploaded_at = models.DateTimeField(null=True, blank=True)
    session_id = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        uploaded_at_cst =  self.uploaded_at.astimezone(ZoneInfo('America/Chicago'))
        file_name = os.path.basename(self.file_name)
        return f"{file_name} uploaded at {uploaded_at_cst.strftime('%H:%M:%S %m-%d-%Y')}"