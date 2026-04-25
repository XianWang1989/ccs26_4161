
from google.appengine.ext import ndb
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @classmethod
    def validate_email(cls, email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

# Usage example
email_to_check = "test@example.com"

if User.validate_email(email_to_check):
    print(f"{email_to_check} is valid.")
else:
    print(f"{email_to_check} is not valid.")
