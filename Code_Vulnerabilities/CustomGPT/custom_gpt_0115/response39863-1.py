
import re
from google.appengine.ext import ndb

# Regular expression for validating an Email
EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'

def is_valid_email(email):
    return re.match(EMAIL_REGEX, email) is not None

class User(ndb.Model):
    email = ndb.StringProperty()

# Usage
email_input = "example@example.com"
if is_valid_email(email_input):
    user = User(email=email_input)
    user.put()
else:
    print("Invalid email address.")
