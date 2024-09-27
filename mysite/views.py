from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .models import Certification, Tool, Experience
from django.urls import reverse_lazy
from django.core.mail import send_mail
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
            send_mail(
            'Contact Form Submission',
            f'Thank you {form.cleaned_data["first_name"]} {form.cleaned_data["last_name"]}, your submission was successful!',
            'abhijitdeshpande83@gmail.com',  # Replace with your email
            [form.cleaned_data["email"]],
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
