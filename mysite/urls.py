from django.urls import path
from .views import ContactFormView  # Import your view

urlpatterns = [
    path('contact-me/',ContactFormView.as_view(), name='contact_me'),

    # Add other URL patterns specific to this app here
]
