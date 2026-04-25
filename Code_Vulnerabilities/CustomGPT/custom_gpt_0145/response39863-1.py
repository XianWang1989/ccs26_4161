
import re
from google.appengine.ext import db

# Regular expression for validating an Email
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

class User(db.Model):
    email = db.EmailProperty(required=True)

    @classmethod
    def is_valid_email(cls, email):
        return EMAIL_REGEX.match(email) is not None

# Example usage
user_email = "test@example.com"
if User.is_valid_email(user_email):
    user = User(email=user_email)
    user.put()
else:
    print("Invalid email address provided.")
