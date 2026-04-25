
import re
from google.appengine.ext import ndb

# Regular expression for validating an Email
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def is_valid_email(email):
    if re.match(email_regex, email):
        return True
    return False

class User(ndb.Model):
    email = ndb.StringProperty()

    @ndb.ComputedProperty
    def is_email_valid(self):
        return is_valid_email(self.email)

# Example usage
user = User(email='test@example.com')

if user.is_email_valid:
    print('Valid email address.')
else:
    print('Invalid email address.')
