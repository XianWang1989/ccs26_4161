
import re
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty()

    @staticmethod
    def is_valid_email(email):
        # Basic regex for email validation
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def put(self, *args, **kwargs):
        if not self.is_valid_email(self.email):
            raise ValueError("Invalid email format")
        super(User, self).put(*args, **kwargs)

# Example usage
try:
    user = User(email='test@example.com')
    user.put()  # Will succeed
    user_invalid = User(email='invalid-email')
    user_invalid.put()  # Will raise ValueError
except ValueError as e:
    print(e)
