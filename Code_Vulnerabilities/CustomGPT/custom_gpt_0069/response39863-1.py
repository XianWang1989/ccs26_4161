
import re
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty()

    @staticmethod
    def is_valid_email(email):
        # Basic regex for validating email
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(regex, email) is not None

# Example usage
user_email = "example@example.com"
if User.is_valid_email(user_email):
    user = User(email=user_email)
    user.put()
else:
    print("Invalid email address.")
