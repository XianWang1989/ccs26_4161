
import re
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty()

def is_valid_email(email):
    # Regular expression for validating an Email
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Example usage
email_to_test = "user@example.com"
if is_valid_email(email_to_test):
    print(f"{email_to_test} is a valid email.")
else:
    print(f"{email_to_test} is not a valid email.")
