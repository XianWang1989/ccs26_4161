
# yourapp/forms.py

class ArchitectDetailsForm(forms.Form):
    business_name = forms.CharField(required=True)
    license_number = forms.CharField(required=True)
    # Add more fields as necessary
