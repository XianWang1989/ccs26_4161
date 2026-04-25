
import re
from google.appengine.ext import ndb

# Regular expression pattern for validating email
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

def is_valid_email(email):
    """Check if the email address is valid."""
    return EMAIL_REGEX.match(email) is not None

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @classmethod
    def create_user(cls, email):
        """Create a new user if the email is valid."""
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
