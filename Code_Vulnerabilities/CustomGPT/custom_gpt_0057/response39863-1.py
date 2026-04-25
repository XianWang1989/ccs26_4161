
import re
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty()

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

def add_user(email):
    if is_valid_email(email):
        user = User(email=email)
        user.put()
        print(f'User with email {email} added successfully.')
    else:
        print(f'Invalid email: {email}')

# Usage example
add_user('test@example.com')  # Valid email
add_user('invalid-email')      # Invalid email
