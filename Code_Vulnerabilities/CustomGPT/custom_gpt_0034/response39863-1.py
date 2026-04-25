
import re
from google.appengine.ext import ndb

# Regular expression for validating an Email
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @classmethod
    def validate_email(cls, email):
        if not email or not EMAIL_REGEX.match(email):
            raise ValueError("Invalid email format.")
        return email

# Example usage
try:
    user = User(email=User.validate_email("test@example.com"))
    user.put()
except ValueError as e:
    print(e)
