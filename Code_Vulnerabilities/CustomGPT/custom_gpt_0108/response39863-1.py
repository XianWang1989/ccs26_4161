
import re
from google.appengine.ext import ndb

# Regular expression for validating an Email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @classmethod
    def validate_email(cls, email):
        if EMAIL_REGEX.match(email):
            return True
        return False

# Usage example
email_to_validate = "user@example.com"
if User.validate_email(email_to_validate):
    print(f"{email_to_validate} is valid.")
else:
    print(f"{email_to_validate} is not valid.")
