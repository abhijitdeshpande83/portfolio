from django.urls import path
from .views import ContactFormView, project, experience, skills, thankyou, download_cv, admin_login 

urlpatterns = [
    path('contact-me/',ContactFormView.as_view(), name='contact_me'),
    path('projects/', project, name='project'),
    path('experience/', experience, name='intro'),
    path('skills/', skills, name='skills'),
    path('thankyou/', thankyou, name='thankyou'),
    path('download_cv/', download_cv, name='download_cv'),
    path('login/', admin_login, name='login'),
    # Add other URL patterns specific to this app here
]
