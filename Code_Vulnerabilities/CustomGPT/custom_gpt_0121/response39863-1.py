
import re
from google.appengine.ext import ndb

# Regular expression for validating an Email
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def is_valid_email(email):
    return re.match(EMAIL_REGEX, email) is not None

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

def add_user(email):
    if is_valid_email(email):
        user = User(email=email)
        user.put()
        return "User added successfully."
    else:
        return "Invalid email address."

# Example usage
print(add_user("example@example.com"))  # Valid email
print(add_user("invalid-email"))         # Invalid email
