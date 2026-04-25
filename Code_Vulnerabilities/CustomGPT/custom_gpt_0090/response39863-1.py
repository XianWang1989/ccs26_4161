
from django import forms

class UserForm(forms.Form):
    email = forms.EmailField()

# Example usage
form = UserForm({'email': 'test@example.com'})

if form.is_valid():
    print("Valid email:", form.cleaned_data['email'])
else:
    print("Errors:", form.errors)
