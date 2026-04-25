
import re
from google.appengine.ext import ndb

# Define a regex pattern for validating email addresses
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @staticmethod
    def is_valid_email(email):
        """Check if the provided email is valid."""
        return EMAIL_REGEX.match(email) is not None

# Example usage
email_to_test = 'example@example.com'

if User.is_valid_email(email_to_test):
    print("Valid email!")
else:
    print("Invalid email!")
