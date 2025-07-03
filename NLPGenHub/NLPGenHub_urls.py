from django.urls import path
from .NLPGenHub_views import test, intent_classify

urlpatterns = [
    path('IntelliQA/', test, name='test'),
    path('intent_classify/', intent_classify, name='intent-classify-api')
]