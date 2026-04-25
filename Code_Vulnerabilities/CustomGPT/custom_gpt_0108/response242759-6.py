
class ArchitectDetailsForm(forms.ModelForm):
    class Meta:
        model = Architect  # your Architect model
        fields = ['business_name', 'license_number', 'address']
