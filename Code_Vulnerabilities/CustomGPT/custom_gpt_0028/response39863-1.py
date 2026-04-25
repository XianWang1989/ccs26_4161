
import re
from google.appengine.ext import ndb

# Regular expression for validating an Email
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def is_valid_email(email):
    """Validate the email using regex."""
    return re.match(EMAIL_REGEX, email) is not None

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @ndb.validates('email')
    def validate_email(self, name, value):
        if not is_valid_email(value):
            raise ndb.ValidationError('Invalid email address.')
        return value

# Example usage
try:
    user = User(email='test@example.com')
    user.put()
    print("Email is valid and user is created.")
except ndb.ValidationError as e:
    print(e)
