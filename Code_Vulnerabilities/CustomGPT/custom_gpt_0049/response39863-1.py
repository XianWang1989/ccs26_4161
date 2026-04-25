
from google.appengine.ext import ndb
from google.appengine.ext.ndb import model
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class User(model.Model):
    email = ndb.StringProperty()

def validate_user_email(email):
    try:
        validate_email(email)
        print("Email is valid.")
    except ValidationError:
        print("Invalid email address.")

# Example usage
user_email = "example@domain.com"
validate_user_email(user_email)
