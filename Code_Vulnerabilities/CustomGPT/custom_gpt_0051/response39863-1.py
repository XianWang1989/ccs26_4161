
import re
from google.appengine.ext import ndb

# Email validation function
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Example NDB model with email validation
class User(ndb.Model):
    email = ndb.StringProperty()

    @classmethod
    def create_user(cls, email):
        if not is_valid_email(email):
            raise ValueError("Invalid email address")
        user = cls(email=email)
        user.put()
        return user

# Usage
try:
    user = User.create_user("example@example.com")
    print("User created:", user.email)
except ValueError as e:
    print(e)
