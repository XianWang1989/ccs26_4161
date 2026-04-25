
import re
from google.appengine.ext import ndb

# Regular expression for validating email addresses
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @property
    def is_valid_email(self):
        return re.match(EMAIL_REGEX, self.email) is not None

# Example usage
def create_user(email):
    user = User(email=email)
    if user.is_valid_email:
        user.put()  # Save to datastore
        return "User created successfully!"
    else:
        return "Invalid email address!"

# Test
print(create_user("test@example.com"))  # Should succeed
print(create_user("invalid-email"))      # Should fail
