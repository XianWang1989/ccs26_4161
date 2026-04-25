
import re
from google.appengine.ext import ndb

# Regular expression for validating an email
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

class User(ndb.Model):
    email = ndb.StringProperty()

    @classmethod
    def validate_email(cls, email):
        if re.match(EMAIL_REGEX, email):
            return True
        return False

# Example usage
email_to_test = "user@example.com"
if User.validate_email(email_to_test):
    print("Valid email!")
else:
    print("Invalid email!")
