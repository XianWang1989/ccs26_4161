
from google.appengine.ext import ndb
from google.appengine.ext.ndb import Model, StringProperty
from django import forms

class UserModel(Model):
    email = StringProperty()

class UserForm(forms.Form):
    email = forms.EmailField()

# Example usage
def validate_email(email_input):
    form = UserForm({'email': email_input})
    if form.is_valid():
        # Email is valid
        print(f"Valid email: {email_input}")
        return True
    else:
        # Email is invalid
        print(f"Invalid email: {form.errors}")
        return False

# Test the function
validate_email('example@example.com')
validate_email('invalid-email')
