from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name','email', 'contact_number', 'message']

        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'contact_number':forms.TextInput(attrs={'class':'form-control'}),
            'message':forms.Textarea(attrs={'class':'form-control','rows': 3}),

        }