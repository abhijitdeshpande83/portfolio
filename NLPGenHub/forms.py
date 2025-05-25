from django import forms
from .models import QueryData

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = QueryData
        fields = ['query_file']

        widgets = {
            'query_file':forms.ClearableFileInput(attrs={'class':'form-control'}),
            }