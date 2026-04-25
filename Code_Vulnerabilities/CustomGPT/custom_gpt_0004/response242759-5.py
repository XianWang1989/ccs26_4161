
class ArchitectDetailsForm(forms.ModelForm):
    class Meta:
        model = ArchitectProfile  # Your model for architect details
        fields = ['business_name', 'website', 'license_number']
