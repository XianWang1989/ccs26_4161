
import re
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty()

def is_valid_email(email):
    # Simple regex for email validation
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Example usage
user_email = "test@example.com"
if is_valid_email(user_email):
    user = User(email=user_email)
    user.put()  # Save to datastore
else:
    print("Invalid email address.")
