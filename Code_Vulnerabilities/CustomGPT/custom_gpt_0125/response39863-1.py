
import re
from google.appengine.ext import db

# Regular expression for validating an Email
EMAIL_REGEX = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

class User(db.Model):
    email = db.EmailProperty(required=True)  # Validates for empty strings

    @classmethod
    def is_valid_email(cls, email):
        return EMAIL_REGEX.match(email) is not None

# Example usage
email_to_check = "test@example.com"
if User.is_valid_email(email_to_check):
    print(f"{email_to_check} is a valid email.")
else:
    print(f"{email_to_check} is not a valid email.")
