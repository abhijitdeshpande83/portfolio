from django.urls import path
from .views import ContactFormView, project, experience, skills, thankyou, download_cv

urlpatterns = [
    path('contact-me/',ContactFormView.as_view(), name='contact_me'),
    path('projects/', project, name='project'),
    path('experience/', experience, name='intro'),
    path('skills/', skills, name='skills'),
    path('thank-you/', thankyou, name='thankyou'),
    path('download-cv/', download_cv, name='download_cv'),
    # Add other URL patterns specific to this app here
]
