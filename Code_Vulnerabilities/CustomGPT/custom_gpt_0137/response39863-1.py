
import re
from google.appengine.ext import ndb

# Regular expression for validating an Email
email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

def is_valid_email(email):
    """Check if the provided email is valid using regex."""
    return email_regex.match(email) is not None

class User(ndb.Model):
    email = ndb.StringProperty()

def create_user(email):
    """Creates a user with the specified email if valid."""
    if is_valid_email(email):
        user = User(email=email)
        user.put()
        print("User created with email:", email)
    else:
        print("Invalid email address:", email)

# Example usage
create_user("test@example.com")  # Valid email
create_user("invalid-email")      # Invalid email
