
import re
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @staticmethod
    def is_valid_email(email):
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(regex, email) is not None

# Example usage
email_to_test = "example@example.com"
if User.is_valid_email(email_to_test):
    print(f"{email_to_test} is a valid email address.")
else:
    print(f"{email_to_test} is not a valid email address.")
