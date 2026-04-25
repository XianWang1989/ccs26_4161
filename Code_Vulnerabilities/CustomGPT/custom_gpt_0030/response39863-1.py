
import re
from google.appengine.ext import ndb

# Regular expression for validating an Email
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# Function to validate email
def is_valid_email(email):
    return re.match(EMAIL_REGEX, email) is not None

# User model with email validation
class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @validates('email')
    def validate_email(self):
        if not is_valid_email(self.email):
            raise ValueError('Invalid email address format.')

# Example of how to use the User model
def create_user(email):
    user = User(email=email)
    try:
        user.validate_email()
        user.put()  # Save the user if validation passes
        print("User created successfully.")
    except ValueError as e:
        print(f"Error: {e}")

# Usage
create_user("test@example.com")  # Valid email
create_user("invalid-email")     # Invalid email
