
import re
from google.appengine.ext import ndb

# Define a custom email validator class
class EmailProperty(ndb.StringProperty):
    def validate(self, value):
        # Check if the email is valid using regex
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, value):
            raise ndb.BadValueError('Invalid email address')
        return value

# Here is how you would use the EmailProperty
class User(ndb.Model):
    email = EmailProperty(required=True)

# Example usage
try:
    user = User(email='test@example.com')
    user.put()
except ndb.BadValueError as e:
    print(e)
