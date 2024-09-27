from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .models import Certification, Tool, Experience
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic.edit import FormView
from .forms import ContactForm
import os

# Create your views here.

def index(request):
    return render(request,'index.html')

def intro(request):
    return render(request, 'about.html')

def project(request):
    return render(request, 'projects.html')

def contact_me(request):
    return render(request, 'contact_me.html')

def skills(request):
    certifications = Certification.objects.all()
    tools = Tool.objects.all()
    params = {'certificate': certifications, 'tool':tools}
    return render(request, 'skills.html', params)

def thankyou(request):
    return render(request, 'thankyou.html')

class ContactFormView(FormView):
    template_name = 'contact_me.html'
    form_class = ContactForm
    success_url = reverse_lazy('thankyou')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            # Send an email
            # Get the user's email
            user_email = form.cleaned_data['email']
            user_first_name = form.cleaned_data['first_name']
            
            # Prepare email content
            subject = 'Confirmation of Your Submission'
            message = f"""
            Dear {user_first_name},

            Thank you for contacting us! We are pleased to inform you that we have successfully received your submission.

            **Submission Details:**
            - **Name:** {user_first_name} {form.cleaned_data['last_name']}
            - **Email:** {form.cleaned_data['email']}
            - **Contact Number:** {form.cleaned_data['contact_number']}
            - **Message:** 
            {form.cleaned_data['message']}

            Your inquiry is important to us, and our team will review your submission and respond to you as soon as possible. We strive to provide timely support and appreciate your patience in this matter.

            If you have any further questions or need immediate assistance, please feel free to reply to this email.

            Best regards,

            [Your Company Name]  
            [Your Company Website]  
            [Your Company Phone Number]  
            """

            # Send email
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,  # Your email
                [user_email],  # Recipient email
                fail_silently=False,
            )
            return super().form_valid(form)
        else:
            # Print or log form errors
            print(form.errors)
            return self.form_invalid(form)
        
def experience(request):
    experiences = Experience.objects.all()
    params = {'experience':experiences}
    return render(request, 'about.html', params)

def download_cv(request):
    return FileResponse(open('media/cv/Resume.docx', 'rb'), as_attachment=True, filename='Resume.docx')

# def tools(request):
#     return render(request, 'tools.html')
