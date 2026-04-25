
import re
from google.appengine.ext import ndb

# Regular expression for validating an Email
email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @classmethod
    def validate_email(cls, email):
        """Validate the email format."""
        return email_regex.match(email) is not None

# Example of using the User model
email_input = "test@example.com"

if User.validate_email(email_input):
    user = User(email=email_input)
    user.put()
    print("Valid email, user created!")
else:
    print("Invalid email format.")
