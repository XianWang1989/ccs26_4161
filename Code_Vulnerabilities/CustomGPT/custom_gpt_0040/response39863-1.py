
import re
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @classmethod
    def is_valid_email(cls, email):
        # Simple regex pattern for email validation
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

# Example usage
email = "test@example.com"
if User.is_valid_email(email):
    user = User(email=email)
    user.put()  # Save to datastore
else:
    print("Invalid email address.")
