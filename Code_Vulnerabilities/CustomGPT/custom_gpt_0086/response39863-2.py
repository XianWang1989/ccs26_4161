
from django.core.validators import email_re
from django.core.exceptions import ValidationError

class User(ndb.Model):
    email = ndb.StringProperty()

    @classmethod
    def is_valid_email(cls, email):
        try:
            email_re(email)
            return True
        except ValidationError:
            return False

# Example usage
email = "example@example.com"
if User.is_valid_email(email):
    print("Valid email address.")
else:
    print("Invalid email address.")
