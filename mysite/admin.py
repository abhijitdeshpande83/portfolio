from django.contrib import admin

# Register your models here.
from .models import Certification, Tool, Contact, Experience, Skill, ProfileAsset

admin.site.register(Certification)
admin.site.register(Tool)
admin.site.register(Contact)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(ProfileAsset)