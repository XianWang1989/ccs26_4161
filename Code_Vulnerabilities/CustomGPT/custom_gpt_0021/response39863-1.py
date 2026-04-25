
import re
from google.appengine.ext import ndb

# Custom email validation function
def is_valid_email(email):
    email_regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    return re.match(email_regex, email) is not None

class User(ndb.Model):
    email = ndb.StringProperty()

    @classmethod
    def validate_email(cls, email):
        if not is_valid_email(email):
            raise ValueError("Invalid email address!")
        return email

# Example usage
try:
    valid_email = User.validate_email("user@example.com")
    user = User(email=valid_email)
    user.put()
    print("Email saved successfully!")
except ValueError as e:
    print(e)
