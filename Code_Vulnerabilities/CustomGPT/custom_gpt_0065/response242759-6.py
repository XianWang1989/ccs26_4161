
class ArchitectDetailsForm(forms.ModelForm):
    class Meta:
        model = Architect  # Your model for business details
        fields = ['business_name', 'address', 'phone_number']
