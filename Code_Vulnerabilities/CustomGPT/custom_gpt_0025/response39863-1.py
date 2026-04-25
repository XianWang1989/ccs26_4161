
import re
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty()

def is_valid_email(email):
    # Regular expression for validating an Email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Usage
email_to_check = "example@mail.com"
if is_valid_email(email_to_check):
    print(f"{email_to_check} is valid.")
else:
    print(f"{email_to_check} is not valid.")
