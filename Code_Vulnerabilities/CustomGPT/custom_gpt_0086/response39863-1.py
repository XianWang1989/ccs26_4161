
import re
from google.appengine.ext import ndb

# Regular expression for validating an Email
email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

class User(ndb.Model):
    email = ndb.StringProperty()

    @classmethod
    def is_valid_email(cls, email):
        return email_regex.match(email) is not None

# Example usage
email = "example@example.com"
if User.is_valid_email(email):
    print("Valid email address.")
else:
    print("Invalid email address.")
