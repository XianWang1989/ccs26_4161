
import re
from google.appengine.ext import db

class User(db.Model):
    email = db.EmailProperty(required=True)

def is_valid_email(email):
    # Simple regex for email validation
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Example usage
email_to_check = "test@example.com"
if is_valid_email(email_to_check):
    print(f"{email_to_check} is valid.")
else:
    print(f"{email_to_check} is invalid.")
