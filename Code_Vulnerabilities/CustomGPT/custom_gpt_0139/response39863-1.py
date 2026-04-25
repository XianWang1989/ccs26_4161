
import re
from google.appengine.ext import ndb

# Define a regular expression for validating an Email
EMAIL_REGEX = re.compile(
    r"(^[a-z0-9_.+-]+@[a-z0-9-]+\.[a-z]{2,}$)", re.I)

# Custom EmailProperty class to validate emails
class EmailProperty(ndb.StringProperty):
    def validate(self, value):
        if not EMAIL_REGEX.match(value):
            raise ValueError(f"{value} is not a valid email address.")

# Example usage of the custom EmailProperty
class User(ndb.Model):
    email = EmailProperty(required=True)

# Function to validate an email
def is_valid_email(email):
    try:
        # Creating a user instance to validate email
        user = User(email=email)
        return True
    except ValueError:
        return False

# Example of usage
if __name__ == "__main__":
    test_email = "example@example.com"

    if is_valid_email(test_email):
        print(f"{test_email} is valid.")
    else:
        print(f"{test_email} is invalid.")
