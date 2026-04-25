
import re

def is_valid_email(email):
    # Simple regex for validating an email
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Example usage
email = "test@example.com"
if is_valid_email(email):
    print(f"{email} is valid.")
else:
    print(f"{email} is invalid.")
