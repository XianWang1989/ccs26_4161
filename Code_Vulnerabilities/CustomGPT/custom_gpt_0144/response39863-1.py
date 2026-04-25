from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField()

# Example usage
data = {'email': 'user@example.com'}
form = EmailForm(data)
if form.is_valid():
    print("Valid email:", form.cleaned_data['email'])
else:
    print("Invalid email:", form.errors)
