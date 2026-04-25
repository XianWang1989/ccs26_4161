
import re
from google.appengine.ext import ndb

# Regular expression for validating an email
email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

class User(ndb.Model):
    email = ndb.StringProperty()

    @classmethod
    def is_valid_email(cls, email):
        return bool(email_regex.match(email))

# Usage example
user_email = 'example@example.com'
if User.is_valid_email(user_email):
    user = User(email=user_email)
    user.put()
else:
    print("Invalid email format")
