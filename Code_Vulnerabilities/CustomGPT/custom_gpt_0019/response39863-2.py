
from django import forms

class MyForm(forms.Form):
    email = forms.EmailField()

# Example usage
form = MyForm({'email': 'user@example.com'})
if form.is_valid():
    print("Email is valid.")
else:
    print("Email is invalid:", form.errors)
