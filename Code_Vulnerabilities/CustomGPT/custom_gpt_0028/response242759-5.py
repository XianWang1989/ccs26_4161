
# forms.py
class ArchitectDetailsForm(forms.ModelForm):
    class Meta:
        model = ArchitectDetails  # Your model for Architect details
        fields = ['business_name', 'address', 'license_number']
