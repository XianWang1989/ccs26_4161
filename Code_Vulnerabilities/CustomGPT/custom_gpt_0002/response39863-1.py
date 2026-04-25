
import re
from google.appengine.ext import ndb

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

class User(ndb.Model):
    email = ndb.StringProperty()

# Usage example
email_to_check = "example@example.com"
if is_valid_email(email_to_check):
    print("Valid email.")
else:
    print("Invalid email.")
