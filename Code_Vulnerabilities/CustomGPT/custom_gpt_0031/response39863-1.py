
from google.appengine.ext import ndb
from django import forms

# Define your model
class User(ndb.Model):
    email = ndb.StringProperty(required=True)

# Create a form for validating the email
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email or "@" not in email:
            raise forms.ValidationError("Please enter a valid email address.")
        return email

# Example usage
def create_user(email):
    form = UserForm({'email': email})
    if form.is_valid():
        user = form.save()
        return user
    else:
        return form.errors
