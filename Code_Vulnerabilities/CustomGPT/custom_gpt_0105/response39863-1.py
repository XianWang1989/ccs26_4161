
import re
from google.appengine.ext import ndb

# Function to validate email
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

class User(ndb.Model):
    email = ndb.StringProperty()

# Example usage
email_to_validate = "test@example.com"
if is_valid_email(email_to_validate):
    user = User(email=email_to_validate)
    user.put()
else:
    print("Invalid email format")
