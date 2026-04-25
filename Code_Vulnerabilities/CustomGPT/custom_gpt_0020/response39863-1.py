
import re
from google.appengine.ext import ndb

# Regular expression for validating an Email
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

def is_valid_email(email):
    """Validate the email format using regex."""
    return email and EMAIL_REGEX.match(email)

class User(ndb.Model):
    email = ndb.StringProperty()

    @classmethod
    def create_user(cls, email):
        if not is_valid_email(email):
            raise ValueError("Invalid email address.")
        user = cls(email=email)
        user.put()  # Save the user to the datastore
        return user

# Example usage
try:
    user = User.create_user("test@example.com")
    print(f"User created with email: {user.email}")
except ValueError as e:
    print(e)
