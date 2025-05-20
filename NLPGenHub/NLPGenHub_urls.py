from django.urls import path
from .NLPGenHub_views import test

urlpatterns = [
    path('IntelliQA/', test, name='test'),
]