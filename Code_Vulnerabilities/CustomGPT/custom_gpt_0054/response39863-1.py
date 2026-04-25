
from django import forms
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        # Further validation can be performed here to check if the email is valid
        return email

# Usage
form = UserForm(data={'email': 'example@example.com'})
if form.is_valid():
    user = form.save()
    print("User created:", user.email)
else:
    print("Errors:", form.errors)
