
import re
from google.appengine.ext import ndb

# Regular expression for validating an Email
EMAIL_REGEX = r"[^@]+@[^@]+\.[^@]+"

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @property
    def is_valid_email(self):
        return re.match(EMAIL_REGEX, self.email) is not None

# Example usage
user = User(email="test@example.com")
if user.is_valid_email:
    print("Valid email address!")
else:
    print("Invalid email address.")
