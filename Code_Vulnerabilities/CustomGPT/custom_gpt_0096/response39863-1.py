
import re
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @classmethod
    def is_valid_email(cls, email):
        # Define a regex for email validation
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

# Usage example
email_to_check = "test@example.com"
if User.is_valid_email(email_to_check):
    print(f"{email_to_check} is a valid email.")
else:
    print(f"{email_to_check} is not a valid email.")
