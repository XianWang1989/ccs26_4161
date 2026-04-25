
import re
from google.appengine.ext import ndb
from google.appengine.ext.ndb import model

# Custom validation function
def validate_email(email):
    email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return email_regex.match(email) is not None

class User(model.Model):
    email = ndb.StringProperty()

# Example of using the custom validation
def create_user(email):
    if not validate_email(email):
        raise ValueError("Invalid email address.")
    user = User(email=email)
    user.put()

# Example usage
try:
    create_user("example@example.com")
    print("User created successfully.")
except ValueError as e:
    print(e)
