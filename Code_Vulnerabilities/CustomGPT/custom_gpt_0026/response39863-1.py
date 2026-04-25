
import re
from google.appengine.ext import ndb

# Regex pattern for validating an email address
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

class User(ndb.Model):
    email = ndb.StringProperty()

    @classmethod
    def is_valid_email(cls, email):
        return EMAIL_REGEX.match(email) is not None

# Example usage
email_to_validate = "test@example.com"
if User.is_valid_email(email_to_validate):
    print("Valid email!")
else:
    print("Invalid email.")
