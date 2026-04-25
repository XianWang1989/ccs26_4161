
import re
from google.appengine.ext import ndb

# Regular expression for validating an Email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

class User(ndb.Model):
    email = ndb.StringProperty()

    @classmethod
    def is_valid_email(cls, email):
        return EMAIL_REGEX.match(email) is not None

# Example usage
user_email = "example@example.com"
if User.is_valid_email(user_email):
    user = User(email=user_email)
    user.put()
    print("Valid email saved.")
else:
    print("Invalid email address.")
