
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty(required=True)

    @property
    def valid_email(self):
        return is_valid_email(self.email)

# Example usage
user = User(email="example@example.com")
if user.valid_email:
    print("Valid email")
else:
    print("Invalid email")
