
import re
from google.appengine.ext import ndb

# Define a simple model with an email property
class User(ndb.Model):
    email = ndb.StringProperty()

# Function to validate email
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

# Usage example
email_input = "example@example.com"
if is_valid_email(email_input):
    user = User(email=email_input)
    user.put()
    print("Email is valid and saved!")
else:
    print("Invalid email format.")
