
import re
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty()

    @staticmethod
    def is_valid_email(email):
        # Regular expression for validating an Email
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(regex, email) is not None

# Example usage
user_email = "test@example.com"

if User.is_valid_email(user_email):
    user = User(email=user_email)
    user.put()  # Store the valid email in the datastore
    print("Email is valid and saved to the datastore.")
else:
    print("Invalid email address.")
