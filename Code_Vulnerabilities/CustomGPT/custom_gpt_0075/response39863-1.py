
import re
from google.appengine.ext import ndb

# Define a model with an EmailProperty
class User(ndb.Model):
    email = ndb.StringProperty()

# Function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Example usage
email_to_test = "test@example.com"
if is_valid_email(email_to_test):
    user = User(email=email_to_test)
    user.put()  # Save the valid email to the datastore
    print("Email saved successfully.")
else:
    print("Invalid email format.")
