
import re
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty()

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Usage
email_to_validate = "test@example.com"
if is_valid_email(email_to_validate):
    user = User(email=email_to_validate)
    user.put()
    print("Valid email saved.")
else:
    print("Invalid email format.")
