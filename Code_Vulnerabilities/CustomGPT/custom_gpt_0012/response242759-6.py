
# myapp/forms.py (add this)
class ArchitectDetailsForm(forms.ModelForm):
    class Meta:
        model = ArchitectDetails  # Make sure to create this model
        fields = ['business_name', 'business_license']
