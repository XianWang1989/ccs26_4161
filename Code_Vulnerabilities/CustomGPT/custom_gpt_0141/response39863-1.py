
import re
from google.appengine.ext import ndb

# Regular expression for validating an Email
email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

def is_valid_email(email):
    """Validate the email using regular expression."""
    return re.match(email_regex, email) is not None

class User(ndb.Model):
    email = ndb.StringProperty()

# Example of using the validator
def create_user(email):
    if not is_valid_email(email):
        raise ValueError("Invalid email format.")
    user = User(email=email)
    user.put()  # Save the user to the datastore

# Example usage
try:
    create_user("test@example.com")  # Valid email
    print("User created successfully.")
    create_user("invalid-email")      # Invalid email
except ValueError as e:
    print(e)
