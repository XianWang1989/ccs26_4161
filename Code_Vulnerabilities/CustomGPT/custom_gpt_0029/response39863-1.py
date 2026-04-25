
import re
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty()

def is_valid_email(email):
    # Simple regex for basic email validation
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

# Example usage
email = "example@domain.com"
if is_valid_email(email):
    user = User(email=email)
    user.put()
    print("Email is valid and saved to the datastore.")
else:
    print("Invalid email address.")
