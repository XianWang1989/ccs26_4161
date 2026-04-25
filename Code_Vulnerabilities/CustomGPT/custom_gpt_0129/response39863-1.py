
import re
from google.appengine.ext import ndb

# Regular expression for validating an Email
email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @classmethod
    def is_valid_email(cls, email):
        return re.match(email_regex, email) is not None

# Example usage
email_to_check = "test@example.com"

if User.is_valid_email(email_to_check):
    print("The email address is valid.")
else:
    print("The email address is invalid.")
