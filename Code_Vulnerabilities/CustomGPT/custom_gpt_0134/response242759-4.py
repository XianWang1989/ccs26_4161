
class BusinessDetailsForm(forms.ModelForm):
    class Meta:
        model = Business  # Your business model
        fields = ['business_name', 'license_number', 'address']  # Add required fields
