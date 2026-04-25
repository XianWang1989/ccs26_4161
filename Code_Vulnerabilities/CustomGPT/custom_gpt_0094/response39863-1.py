
import re
from google.appengine.ext import ndb

# Regular expression for validating an Email
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def is_valid_email(email):
    return re.match(EMAIL_REGEX, email) is not None

class User(ndb.Model):
    email = ndb.StringProperty()

# Example usage
email_to_validate = "test@example.com"

if is_valid_email(email_to_validate):
    user = User(email=email_to_validate)
    user.put()
    print("Email is valid and saved!")
else:
    print("Invalid email address.")
