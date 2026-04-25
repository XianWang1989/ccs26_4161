
import re
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty()

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

# Example usage
email_to_check = "example@example.com"
if is_valid_email(email_to_check):
    print(f"{email_to_check} is valid.")
else:
    print(f"{email_to_check} is not valid.")
