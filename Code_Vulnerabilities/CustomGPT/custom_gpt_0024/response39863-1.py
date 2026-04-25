
import re
from google.appengine.ext import db

# Regular expression for validating an Email
EMAIL_REGEX = r"[^@]+@[^@]+\.[^@]+"

class User(db.Model):
    email = db.EmailProperty(required=True)

    @staticmethod
    def is_valid_email(email):
        return re.match(EMAIL_REGEX, email) is not None

# Example usage
email_input = "example@test.com"
if User.is_valid_email(email_input):
    user = User(email=email_input)
    user.put()
    print("Email is valid and user created.")
else:
    print("Invalid email address.")
