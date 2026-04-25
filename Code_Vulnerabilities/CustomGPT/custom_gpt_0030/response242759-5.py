
# forms.py
class ArchitectDetailsForm(forms.ModelForm):
    class Meta:
        model = Architect  # Replace with your model
        fields = ['business_name', 'license_number']  # Your specific fields
