
import re
from google.appengine.ext import ndb

def is_valid_email(email):
    # Regular expression for validating an Email
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

class User(ndb.Model):
    email = ndb.StringProperty()

    @classmethod
    def add_user(cls, email):
        if is_valid_email(email):
            user = cls(email=email)
            user.put()
            return "User added."
        else:
            return "Invalid email address."

# Example usage
result = User.add_user("test@example.com")
print(result)  # Output: User added.

result = User.add_user("invalid-email")
print(result)  # Output: Invalid email address.
