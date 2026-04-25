
import re
from google.appengine.ext import ndb

# Regular expression for validating an Email
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @classmethod
    def is_valid_email(cls, email):
        return re.match(EMAIL_REGEX, email) is not None

# Example usage
def add_user(email):
    if User.is_valid_email(email):
        user = User(email=email)
        user.put()  # Store user in the database
        return f"User with email {email} added successfully!"
    else:
        return "Invalid email format!"

# Example on calling the function
print(add_user("test@example.com"))  # Valid email
print(add_user("invalid-email.com"))  # Invalid email
