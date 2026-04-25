
# forms.py
class ArchitectDetailsForm(forms.ModelForm):
    class Meta:
        model = ArchitectDetails
        fields = ['business_name', 'license_number', ...]
