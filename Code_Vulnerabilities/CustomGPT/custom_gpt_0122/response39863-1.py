
import re
from google.appengine.ext import ndb

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

class User(ndb.Model):
    email = ndb.StringProperty()

    @classmethod
    def validate_email(cls, email):
        if not is_valid_email(email):
            raise ValueError("Invalid email address.")

# Example usage
try:
    email_to_validate = "test@example.com"
    User.validate_email(email_to_validate)
    print("Email is valid.")
except ValueError as e:
    print(e)
