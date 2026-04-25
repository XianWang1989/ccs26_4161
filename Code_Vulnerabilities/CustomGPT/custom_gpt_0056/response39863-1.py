
import re
from google.appengine.ext import ndb

def is_valid_email(email):
    # Basic regex for email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

class User(ndb.Model):
    email = ndb.StringProperty()

    @staticmethod
    def validate_email(email):
        if not is_valid_email(email):
            raise ValueError("Invalid email address")

# Example usage
try:
    email = "test@example.com"
    User.validate_email(email)
    user = User(email=email)
    user.put()
    print("Email is valid and user created.")
except ValueError as e:
    print(e)
