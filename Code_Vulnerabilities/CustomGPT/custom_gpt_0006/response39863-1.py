
import re
from google.appengine.ext import ndb
from google.appengine.ext.ndb import model

class User(model.Model):
    email = model.EmailProperty()

    @classmethod
    def validate_email(cls, email):
        # Regular expression for validating an Email
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

# Example usage
email_to_check = "example@example.com"

if User.validate_email(email_to_check):
    print("Valid email")
else:
    print("Invalid email")
