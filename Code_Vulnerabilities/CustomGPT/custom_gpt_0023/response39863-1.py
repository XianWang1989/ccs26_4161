
import re
from google.appengine.ext import ndb

# Custom validation function
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @classmethod
    def create(cls, email):
        if not is_valid_email(email):
            raise ValueError('Invalid email format')
        return cls(email=email)

# Usage example
try:
    new_user = User.create('example@example.com')
    print("User created with email:", new_user.email)
except ValueError as e:
    print(e)
