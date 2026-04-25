
import re
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty()

    @staticmethod
    def is_valid_email(email):
        # Simple regex pattern for validating an email
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

# Example usage
def add_user(email):
    if User.is_valid_email(email):
        user = User(email=email)
        user.put()
        print("User added with email:", email)
    else:
        print("Invalid email address:", email)

# Test the function
add_user("test@example.com")  # Valid email
add_user("invalid-email")      # Invalid email
