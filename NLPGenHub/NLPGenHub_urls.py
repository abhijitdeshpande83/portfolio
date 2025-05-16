from django.urls import path
from .NLPGenHub_views import test, upload_file

urlpatterns = [
    path('test/', test, name='test'),
    path('upload/', upload_file, name='upload_form')
]