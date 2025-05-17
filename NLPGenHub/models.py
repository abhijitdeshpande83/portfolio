from django.db import models

# Create your models here.

class QueryData(models.Model):
    query_file = models.FileField(upload_to='NLP_data',blank=True, null=True)
    file_hash = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.query_file.name
