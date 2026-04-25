
import re
from google.appengine.ext import ndb

# Regex for validating email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @staticmethod
    def is_valid_email(email):
        """Check if the email is valid."""
        return email and EMAIL_REGEX.match(email)

# Example usage
user_email = "test@example.com"

if User.is_valid_email(user_email):
    user = User(email=user_email)
    user.put()  # Save to the datastore
    print("Email is valid and user saved.")
else:
    print("Invalid email address.")
