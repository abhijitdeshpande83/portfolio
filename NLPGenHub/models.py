from django.db import models

# Create your models here.

class QueryData(models.Model):
    query_file = models.FileField(upload_to='NLP_data',blank=True, null=True)
