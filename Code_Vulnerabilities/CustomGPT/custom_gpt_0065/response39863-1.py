
import re
from google.appengine.ext import ndb

# Function to validate email
def is_valid_email(email):
    # Regular expression for validating an Email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))

# Example usage
email = "example@example.com"
if is_valid_email(email):
    print(f"{email} is a valid email.")
else:
    print(f"{email} is not a valid email.")

# NDB Model for storing emails
class User(ndb.Model):
    email = ndb.StringProperty()

# Usage in a model
user = User(email=email)
if is_valid_email(user.email):
    user.put()
else:
    print("Invalid email, not saved.")
