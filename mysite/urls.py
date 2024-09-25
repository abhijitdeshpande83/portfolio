from django.urls import path
from .views import ContactFormView, project  # Import your view

urlpatterns = [
    path('contact-me/',ContactFormView.as_view(), name='contact_me'),
    path('projects/', project, name='project'),
    # Add other URL patterns specific to this app here
]
