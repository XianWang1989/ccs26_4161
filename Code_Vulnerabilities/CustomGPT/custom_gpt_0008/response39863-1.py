
import re
from google.appengine.ext import ndb

# Regular expression for validating an email address
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

class User(ndb.Model):
    email = ndb.StringProperty()

    @property
    def is_valid_email(self):
        return EMAIL_REGEX.match(self.email) is not None

# Usage example
user = User(email="test@example.com")
if user.is_valid_email:
    print("Valid email")
else:
    print("Invalid email")
