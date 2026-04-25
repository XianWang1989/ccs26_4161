
import re
from google.appengine.ext import ndb

# Regex pattern for validating email addresses
EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @classmethod
    def is_valid_email(cls, email):
        return re.match(EMAIL_REGEX, email) is not None

# Example usage
email_to_validate = "example@example.com"
if User.is_valid_email(email_to_validate):
    print(f"{email_to_validate} is valid.")
else:
    print(f"{email_to_validate} is not valid.")
