
import re
from google.appengine.ext import ndb

# Regular expression for validating an Email
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

def is_valid_email(email):
    return re.match(EMAIL_REGEX, email) is not None

class User(ndb.Model):
    email = ndb.StringProperty()

    @classmethod
    def create_user(cls, email):
        if not is_valid_email(email):
            raise ValueError("Invalid email address")
        user = cls(email=email)
        user.put()

# Example usage:
try:
    User.create_user("test@example.com")
    print("User created successfully.")
except ValueError as e:
    print(e)
