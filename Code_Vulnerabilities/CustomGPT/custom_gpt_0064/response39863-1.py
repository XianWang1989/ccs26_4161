
import re
from google.appengine.ext import ndb

# Custom email validation function
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

class User(ndb.Model):
    email = ndb.StringProperty()

    @classmethod
    def validate_email(cls, email):
        if not is_valid_email(email):
            raise ValueError('Invalid email address: {}'.format(email))

# Example usage
try:
    email_input = 'user@example.com'  # Replace with input email
    User.validate_email(email_input)
    user = User(email=email_input)
    user.put()  # Save to Datastore
except ValueError as ve:
    print(ve)
