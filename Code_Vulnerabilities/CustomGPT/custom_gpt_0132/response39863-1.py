
import re
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty()

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Example usage
user_email = "example@example.com"
if is_valid_email(user_email):
    user = User(email=user_email)
    user.put()
else:
    print("Invalid email address.")
