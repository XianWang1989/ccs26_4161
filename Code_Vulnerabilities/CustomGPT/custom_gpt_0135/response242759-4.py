
# forms.py
class ArchitectBusinessDetailsForm(forms.ModelForm):
    class Meta:
        model = UserProfile  # or another model for business details
        fields = ['business_name', 'license_number', 'address', ...]
