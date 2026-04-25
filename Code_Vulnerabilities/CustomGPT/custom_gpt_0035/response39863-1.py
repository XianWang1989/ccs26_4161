
import re
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @classmethod
    def validate_email(cls, email):
        # Simple regex for validating an email
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(regex, email) is not None

    def put(self, *args, **kwargs):
        if not self.validate_email(self.email):
            raise ValueError("Invalid email address")
        super(User, self).put(*args, **kwargs)

# Usage
try:
    user = User(email='test@example.com')
    user.put()
    print("User created successfully!")
except ValueError as e:
    print(e)
