from django import forms
from .models import Report
from reports.models import Resource


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['incident_type', 'location', 'description', 'contact_info']
        widgets = {
            'incident_type': forms.RadioSelect(),  # Display incident types as radio buttons
            'location': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'description': forms.Textarea(attrs={'rows': 6, 'cols': 40}),
            'contact_info': forms.TextInput(attrs={'placeholder': 'Optional: Contact information'}),
        }

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'description', 'file_url', ]      
