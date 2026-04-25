
import re
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @staticmethod
    def is_valid_email(email):
        # Regular expression for validating an Email
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

# Example usage
user_email = "example@example.com"

if User.is_valid_email(user_email):
    user = User(email=user_email)
    user.put()
    print("User saved successfully.")
else:
    print("Invalid email address.")
