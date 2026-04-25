
from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField()

# Example usage
form = EmailForm({'email': 'example@example.com'})
if form.is_valid():
    print("Valid email")
else:
    print("Invalid email:", form.errors)
