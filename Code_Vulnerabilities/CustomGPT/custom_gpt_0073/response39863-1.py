
import re

def is_valid_email(email):
    # Basic regex for simple email validation
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(email_regex, email):
        return True
    return False

# Example usage
email = "test@example.com"
if is_valid_email(email):
    print(f"{email} is valid.")
else:
    print(f"{email} is invalid.")
