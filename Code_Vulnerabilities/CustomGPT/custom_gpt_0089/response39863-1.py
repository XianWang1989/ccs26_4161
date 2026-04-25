
import re
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty()

    @classmethod
    def validate_email(cls, email):
        # Simple regex for email validation
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(regex, email):
            raise ValueError('Invalid email address')
        return email

    @classmethod
    def create_user(cls, email):
        cls.validate_email(email)
        user = User(email=email)
        user.put()  # Save to the datastore
        return user

# Example usage
try:
    user = User.create_user("example@example.com")
    print("User created with email:", user.email)
except ValueError as e:
    print(e)
