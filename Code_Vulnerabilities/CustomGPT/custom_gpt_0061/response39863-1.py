
import re
from google.appengine.ext import ndb

# Regular expression for validating an Email
email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

class User(ndb.Model):
    email = ndb.StringProperty()

    @classmethod
    def is_valid_email(cls, email):
        """Check if the provided email is valid."""
        return email_pattern.match(email) is not None

# Usage example:
user_email = "example@example.com"
if User.is_valid_email(user_email):
    user = User(email=user_email)
    user.put()
    print("Email is valid and saved.")
else:
    print("Invalid email address.")
