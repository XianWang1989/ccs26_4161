
import re
from google.appengine.ext import ndb

# Regular expression for validating an Email
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

class User(ndb.Model):
    email = ndb.StringProperty()

    @classmethod
    def is_valid_email(cls, email):
        return re.match(EMAIL_REGEX, email) is not None

# Example usage
email_input = "example@example.com"
if User.is_valid_email(email_input):
    user = User(email=email_input)
    user.put()
    print("Email is valid and saved.")
else:
    print("Invalid email address.")
