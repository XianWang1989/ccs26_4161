
import re
from google.appengine.ext import ndb

# Regular expression for validating an Email
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @classmethod
    def validate_email(cls, email):
        if not re.match(EMAIL_REGEX, email):
            raise ValueError("Invalid email address")
        return True

# Example of usage:
try:
    user_email = "test@example.com"
    User.validate_email(user_email)
    user = User(email=user_email)
    user.put()  # Save the user to the datastore
except ValueError as e:
    print(e)
