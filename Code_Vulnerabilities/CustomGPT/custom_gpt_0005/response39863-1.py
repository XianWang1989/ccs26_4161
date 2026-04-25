
import re
from google.appengine.ext import ndb

# Email validation regex pattern
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @classmethod
    def is_valid_email(cls, email):
        return re.match(EMAIL_REGEX, email) is not None

# Example usage
email_to_test = "example@example.com"
if User.is_valid_email(email_to_test):
    print("Valid email")
else:
    print("Invalid email")
