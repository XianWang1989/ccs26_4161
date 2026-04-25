
# forms.py
class BusinessDetailsForm(forms.ModelForm):
    class Meta:
        model = BusinessDetails  # Your model
        fields = ['company_name', 'address', 'phone_number']
