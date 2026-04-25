
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Example usage
email = "user@example.com"
if is_valid_email(email):
    print(f"{email} is valid.")
else:
    print(f"{email} is invalid.")
