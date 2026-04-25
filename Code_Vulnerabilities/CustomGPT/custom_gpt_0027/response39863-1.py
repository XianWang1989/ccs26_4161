
import re
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @staticmethod
    def is_valid_email(email):
        # Basic regex for validating an email
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(regex, email) is not None

# Usage Example
user_email = "test@example.com"
if User.is_valid_email(user_email):
    user = User(email=user_email)
    user.put()
else:
    print("Invalid email address.")
