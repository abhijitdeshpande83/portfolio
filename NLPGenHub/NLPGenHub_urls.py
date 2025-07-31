from django.urls import path
from .NLPGenHub_views import rag_intelliqa, intent_classify

urlpatterns = [
    path('IntelliQA/', rag_intelliqa, name='rag_intelliqa'),
    path('intent_classify/', intent_classify, name='intent-classify-api')
]