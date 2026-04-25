
from google.appengine.ext import ndb
import re

class User(ndb.Model):
    email = ndb.StringProperty()

    @classmethod
    def validate_email(cls, email):
        # Regex for validating an email
        email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        return email_regex.match(email)

    @classmethod
    def create_user(cls, email):
        if cls.validate_email(email):
            user = cls(email=email)
            user.put()  # Save to the datastore
            return "User created successfully!"
        else:
            return "Invalid email format!"

# Example usage
response = User.create_user("test@example.com")
print(response)  # Output: User created successfully!
