
from google.appengine.ext import ndb
from google.appengine.ext.ndb import model
from django import forms

# Define your data model
class UserModel(ndb.Model):
    email = ndb.StringProperty(required=True)

# Create a form class
class UserForm(forms.Form):
    email = forms.EmailField()

# Example function to validate email
def validate_email(email):
    form = UserForm({'email': email})
    if form.is_valid():
        return True, None
    else:
        return False, form.errors

# Sample usage
email = "test@example.com"
is_valid, error = validate_email(email)

if is_valid:
    print("Valid email!")
else:
    print(f"Invalid email: {error}")
