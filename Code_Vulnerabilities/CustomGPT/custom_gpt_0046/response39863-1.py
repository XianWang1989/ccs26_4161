
import re
from google.appengine.ext import ndb

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

class User(ndb.Model):
    email = ndb.StringProperty()

    @staticmethod
    def is_valid_email(email):
        return EMAIL_REGEX.match(email) is not None

# Example usage
user_email = "example@example.com"
if User.is_valid_email(user_email):
    print("Valid email address.")
else:
    print("Invalid email address.")
