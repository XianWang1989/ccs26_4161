
import re
from google.appengine.ext import ndb

# Define a regex pattern for validating email
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @classmethod
    def is_valid_email(cls, email):
        return EMAIL_REGEX.match(email) is not None

# Example usage
email_input = "test@example.com"
if User.is_valid_email(email_input):
    user = User(email=email_input)
    user.put()
    print("Email is valid and saved!")
else:
    print("Invalid email address.")
