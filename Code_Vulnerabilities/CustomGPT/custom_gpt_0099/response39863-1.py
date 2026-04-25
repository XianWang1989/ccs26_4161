
import re
from google.appengine.ext import ndb

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @classmethod
    def create_user(cls, email):
        if not is_valid_email(email):
            raise ValueError("Invalid email address")
        user = User(email=email)
        user.put()  # Save to the datastore

# Example usage
try:
    User.create_user("test@example.com")
    print("User created successfully!")
except ValueError as e:
    print(e)
