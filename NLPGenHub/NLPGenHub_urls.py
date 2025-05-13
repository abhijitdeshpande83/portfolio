from django.urls import path
from .NLPGenHub_views import test

urlpatterns = [
    path('test/', test, name='test'),
]