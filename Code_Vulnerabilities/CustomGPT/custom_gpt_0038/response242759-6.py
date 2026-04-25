
# forms.py

class BusinessDetailsForm(forms.ModelForm):
    class Meta:
        model = BusinessDetails  # Your model here
        fields = ['business_name', 'license_number', ...]  # Add your fields
