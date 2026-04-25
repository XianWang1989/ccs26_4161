
import re
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty()

def is_valid_email(email):
    # Regular expression for validating an Email
    email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return re.match(email_regex, email) is not None

# Example usage
email_to_test = 'test@example.com'
if is_valid_email(email_to_test):
    user = User(email=email_to_test)
    user.put()  # Save to Datastore
    print("Email is valid and saved.")
else:
    print("Invalid email address.")
