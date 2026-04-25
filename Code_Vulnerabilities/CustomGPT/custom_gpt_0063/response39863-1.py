
import re

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Example usage
email = "test@example.com"
if is_valid_email(email):
    print(f"{email} is valid.")
else:
    print(f"{email} is invalid.")
