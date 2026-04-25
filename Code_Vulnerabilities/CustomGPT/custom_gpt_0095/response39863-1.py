
import re
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty()

    @classmethod
    def is_valid_email(cls, email):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

# Usage example
user_email = "test@example.com"

if User.is_valid_email(user_email):
    user = User(email=user_email)
    user.put()  # Save the user to the datastore
else:
    print("Invalid email address.")
