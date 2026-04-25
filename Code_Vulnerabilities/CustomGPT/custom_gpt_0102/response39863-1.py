
import re
from google.appengine.ext import ndb

# Define your model with a StringProperty to store emails
class User(ndb.Model):
    email = ndb.StringProperty(required=True)

# Function to validate email format
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.edu$'
    return re.match(regex, email) is not None

# Example usage
email_input = "user@example.edu"

if is_valid_email(email_input):
    user = User(email=email_input)
    user.put()  # Save to datastore
    print("Email is valid and saved.")
else:
    print("Invalid email format.")
