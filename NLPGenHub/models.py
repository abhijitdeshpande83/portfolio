import os
from django.db import models

# Create your models here.

class QueryData(models.Model):
    query_file = models.FileField(upload_to='NLP_data',blank=True, null=True)
    file_hash = models.CharField(max_length=64, unique=True, primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query_file.name
    
    def delete(self, *args, **kwargs):
        if self.query_file and os.path.isfile(self.query_file.path):
            os.remove(self.query_file.path)         # removes file from file system
        super().delete(*args, **kwargs)             # removes file reference path from DB
