
# forms.py
class BusinessDetailsForm(forms.ModelForm):
    class Meta:
        model = YourBusinessModel  # Replace with your actual model
        fields = ['business_name', 'address', 'contact_number']
