from django.shortcuts import render
from django.http import HttpResponse, FileResponse, Http404
from .models import Certification, Tool, Experience, Skill, ProfileAsset, Project
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic.edit import FormView
from .forms import ContactForm
import os

# Create your views here.

def index(request):
    profile_data = ProfileAsset.objects.all().first()
    return render(request, 'index.html',{'profile_data': profile_data})


def project(request):
    projects = Project.objects.all().order_by('project_number')
    
    return render(request, 'projects.html', {'projects': projects})

def contact_me(request):
    return render(request, 'contact_me.html')

def skills(request):
    certifications = Certification.objects.all().order_by('certification_rank')
    tools = Tool.objects.all().order_by('tool_rank')
    skills = Skill.objects.all().order_by('row_number', 'column_number')
    total_rows = Skill.objects.values_list('row_number', flat=True).distinct().count()
    row_numbers = list(range(1, total_rows + 1))  # Create a list of number of rows


    params = {'certificate': certifications, 'tool':tools,  'skill': skills, 'row_numbers': row_numbers} 
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
    experiences = Experience.objects.all().order_by('experience_rank')
    params = {'experience':experiences}
    return render(request, 'experience.html', params)

def download_cv(request):
    resume = ProfileAsset.objects.all().first()
    if resume.resume_file:
        file_path = resume.resume_file.path
        file_name = resume.resume_file.name
        _, file_extension = os.path.splitext(file_name) 
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=f"{"Abhijit_Deshpande_Resume"}{file_extension}")
    else:
        raise Http404("Resume file not found.")

 