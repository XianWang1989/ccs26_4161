
from google.appengine.ext import ndb
from django import forms

# Define a model with an EmailField
class UserModel(ndb.Model):
    email = ndb.StringProperty()  # This does not validate

# Create a Django form for email validation
class UserForm(forms.Form):
    email = forms.EmailField()  # This will validate the email format

# Usage
def validate_user_email(email):
    form = UserForm({'email': email})
    if form.is_valid():
        print("Valid email:", email)
        # You can save the email to your model here
        user = UserModel(email=email)
        user.put()
    else:
        print("Invalid email:", form.errors)

# Example of testing the function
validate_user_email("test@example.com")
validate_user_email("invalid-email")
