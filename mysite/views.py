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
            user_last_name = form.cleaned_data['last_name']
            full_name = f"{user_first_name} {user_last_name}"
            
            # Prepare email content
            subject = "Submission Successful 🙂"
            message = f"""
            <p>Dear {full_name},</p>

            <p>I appreciate you taking the time to share your thoughts with me, and I’m happy to confirm that 
            I have received your feedback.</p>

            <h3>Submission Details:</h3>
            <ul>
                <li><strong>Name:</strong> {full_name}</li>
                <li><strong>Email:</strong> {user_email}</li>
                <li><strong>Contact Number:</strong> {form.cleaned_data['contact_number']}</li>
                <li><strong>Message:</strong> {form.cleaned_data['message']}</li>
            </ul>

            <p>Your feedback is incredibly important to me, and I genuinely value your insights regarding my work. I am eager 
            to hear your thoughts and suggestions, as they will help me improve and grow.</p>

            <p>If you have any further comments or questions, please don't hesitate to reach out. 
            I truly appreciate your time and support in this process.</p>

            <p><em>Best regards,</em><br>
            <em>Abhijit Deshpande</em><br>
            <a href="https://www.linkedin.com/in/abhijit-deshpande/">LinkedIn</a><br>
            <em>+1 817-271-2819</em></p>
            """

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,  # Your email
                [user_email],  # Recipient email
                fail_silently=False,
                html_message=message  # This parameter allows HTML content
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
