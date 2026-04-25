
import re
from google.appengine.ext import ndb

# Email validation regex
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def is_valid_email(email):
    return re.match(EMAIL_REGEX, email) is not None

# Example NDB model using Email validation
class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @classmethod
    def create_user(cls, email):
        if not is_valid_email(email):
            raise ValueError("Invalid email address")
        user = cls(email=email)
        user.put()
        return user

# Example usage
try:
    user = User.create_user("test@example.com")
    print("User created with email:", user.email)
except ValueError as e:
    print(e)
