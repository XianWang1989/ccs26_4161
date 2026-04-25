
import re
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty()

    @staticmethod
    def is_valid_email(email):
        # Define a simple regex for validating an email
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

# Usage example
user_email = "example@example.com"
if User.is_valid_email(user_email):
    user = User(email=user_email)
    user.put()
else:
    print("Invalid email address.")
