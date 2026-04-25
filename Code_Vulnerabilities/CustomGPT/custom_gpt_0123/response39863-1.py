
import re
from google.appengine.ext import ndb

# Define a regex pattern for validating email addresses
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @classmethod
    def is_valid_email(cls, email):
        return re.match(EMAIL_REGEX, email) is not None

# Usage
email_input = "user@example.com"

if User.is_valid_email(email_input):
    user = User(email=email_input)
    user.put()  # Save the valid email
else:
    print("Invalid email format.")
