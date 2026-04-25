
import re
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty()

    @classmethod
    def is_valid_email(cls, email):
        # Simple regex for email validation
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

# Example usage
user_email = 'test@example.com'
if User.is_valid_email(user_email):
    user = User(email=user_email)
    user.put()
    print("Valid email and user saved.")
else:
    print("Invalid email.")
