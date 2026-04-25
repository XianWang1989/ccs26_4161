
from django import forms

class ArchitectDetailsForm(forms.Form):
    business_name = forms.CharField(max_length=100)
    license_number = forms.CharField(max_length=50)
