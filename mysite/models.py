from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Certification(models.Model):
    certification_id = models.AutoField(primary_key=True)
    certification_rank = models.IntegerField(default=99, blank=True) 
    certification_name = models.CharField(max_length=100, default='')
    certification_logo = models.FileField(upload_to='certifications', default='')
    verification_url = models.CharField(max_length=200, default='')

    def __str__(self) -> str:
        return self.certification_name

class Tool(models.Model):
    tool_id = models.AutoField(primary_key=True)
    tool_rank = models.IntegerField(default=99, blank=True) 
    tool_name = models.CharField(max_length=100, default='')
    tool_logo = models.FileField(upload_to='tools', default='') 

    def __str__(self) -> str:
        return self.tool_name
    
class Contact(models.Model):
    first_name = models.CharField(max_length=15, default='')
    last_name =  models.CharField(max_length=15, default='', blank=True,)
    email = models.EmailField(max_length=50)
    contact_number = PhoneNumberField(blank=True, null=True)
    message = models.TextField(max_length=2500,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True) 


    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.get_full_name()} {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
    

class Experience(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50, default='')
    company_experience = models.TextField(default='',blank=True)
    timeline = models.CharField(max_length=20, default='', blank=True)
    role = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.company_name