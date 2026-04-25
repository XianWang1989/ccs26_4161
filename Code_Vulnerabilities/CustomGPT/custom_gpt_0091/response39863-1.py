
import re
from google.appengine.ext import ndb

def is_valid_email(email):
    # Simple regex for validating an email address
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

class User(ndb.Model):
    email = ndb.StringProperty()

    @classmethod
    def create_user(cls, email):
        if not is_valid_email(email):
            raise ValueError("Invalid email address")
        user = cls(email=email)
        user.put()  # Save to the datastore

# Example usage
try:
    User.create_user("example@domain.com")
    print("User created successfully!")
except ValueError as e:
    print(e)
