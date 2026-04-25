
import re
from google.appengine.ext import db

# Regular expression for validating an Email
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def is_valid_email(email):
    """Check if the provided email is valid."""
    if re.match(EMAIL_REGEX, email):
        return True
    return False

class User(db.Model):
    email = db.StringProperty(required=True)

    def put(self, *args, **kwargs):
        if not is_valid_email(self.email):
            raise ValueError("Invalid email address!")
        super(User, self).put(*args, **kwargs)

# Example usage
try:
    user = User(email="test@example.com")
    user.put()  # Will raise ValueError if email is invalid
except ValueError as ve:
    print(ve)
