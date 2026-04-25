
import re
from google.appengine.ext import ndb

# Function to validate email
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

class User(ndb.Model):
    email = ndb.StringProperty()

# Example usage
user_email = "example@example.com"

if is_valid_email(user_email):
    user = User(email=user_email)
    user.put()
    print("Email saved!")
else:
    print("Invalid email address.")
