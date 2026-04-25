
import re
from google.appengine.ext import ndb

# Define a valid email regex pattern
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @classmethod
    def is_valid_email(cls, email):
        return re.match(EMAIL_REGEX, email) is not None

# Example usage
user_email = "example@example.com"
if User.is_valid_email(user_email):
    user = User(email=user_email)
    user.put()
    print("Email is valid and user created.")
else:
    print("Invalid email format.")
