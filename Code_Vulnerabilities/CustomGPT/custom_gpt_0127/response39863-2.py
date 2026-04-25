
from google.appengine.ext import ndb

class User(ndb.Model):
    email = ndb.StringProperty()

    def put(self, *args, **kwargs):
        if not is_valid_email(self.email):
            raise ValueError("Invalid email address.")
        super(User, self).put(*args, **kwargs)
