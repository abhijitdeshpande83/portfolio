from django.contrib import admin

# Register your models here.
from .models import QueryData, ResourceCleanupLog

admin.site.register(QueryData)
admin.site.register(ResourceCleanupLog)
