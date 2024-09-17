from django.contrib import admin

# Register your models here.
from .models import Certification, Tool, Contact, Experience

admin.site.register(Certification)
admin.site.register(Tool)
admin.site.register(Contact)
admin.site.register(Experience)