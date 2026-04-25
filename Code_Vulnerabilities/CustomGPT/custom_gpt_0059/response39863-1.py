
import re
from google.appengine.ext import ndb

# Regex pattern for validating email
EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @classmethod
    def validate_email(cls, email):
        return re.match(EMAIL_REGEX, email) is not None

# Example usage
def add_user(email):
    if User.validate_email(email):
        new_user = User(email=email)
        new_user.put()
        print("User added successfully.")
    else:
        print("Invalid email address.")

# Example email
add_user("test@example.com")
