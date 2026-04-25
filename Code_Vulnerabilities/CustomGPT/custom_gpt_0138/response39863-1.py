
import re
from google.appengine.ext import ndb

def is_valid_email(email):
    # Simple regex for basic email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

class User(ndb.Model):
    email = ndb.StringProperty()

# Example usage
user_email = "test@example.com"
if is_valid_email(user_email):
    user = User(email=user_email)
    user.put()
    print("Valid email saved.")
else:
    print("Invalid email format.")
