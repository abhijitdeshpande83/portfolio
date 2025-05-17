from django.urls import path
from .NLPGenHub_views import test, upload_file

urlpatterns = [
    path('test/', test, name='test'),
]