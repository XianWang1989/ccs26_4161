
from google.appengine.ext import ndb
from google.appengine.ext.ndb import model
from django import forms

class UserProfile(ndb.Model):
    email = ndb.StringProperty()

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not forms.EmailField().clean(email):
            raise forms.ValidationError("Invalid email address")
        return email

# Usage example
form_data = {'email': 'test@example.com'}
form = UserProfileForm(data=form_data)

if form.is_valid():
    user_profile = form.save()
    print("Email is valid:", user_profile.email)
else:
    print("Errors:", form.errors)
