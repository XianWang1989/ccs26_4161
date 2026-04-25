
import re
from google.appengine.ext import ndb

def is_valid_email(email):
    # Simple regex for email validation
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

class User(ndb.Model):
    email = ndb.StringProperty()

    @ndb.validated_property
    def validated_email(self):
        if not is_valid_email(self.email):
            raise ValueError("Invalid email format")
        return self.email

# Example usage
user = User(email="example@example.com")
try:
    valid_email = user.validated_email
    print("Email is valid:", valid_email)
except ValueError as e:
    print(e)
