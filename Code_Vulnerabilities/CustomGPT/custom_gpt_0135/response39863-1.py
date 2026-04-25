
import re
from google.appengine.ext import ndb
from google.appengine.ext.ndb import model

# Regular expression for validating an Email
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

class UserModel(ndb.Model):
    email = ndb.StringProperty(required=True)

    @classmethod
    def is_valid_email(cls, email):
        return EMAIL_REGEX.match(email) is not None

# Example usage
user_email = "example@example.com"
if UserModel.is_valid_email(user_email):
    user = UserModel(email=user_email)
    user.put()
    print("Email saved successfully.")
else:
    print("Invalid email address.")
