
import re

def is_valid_email(email):
    # Basic regex for validating an email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Example usage
email_to_check = "example@example.com"
if is_valid_email(email_to_check):
    print(f"{email_to_check} is a valid email.")
else:
    print(f"{email_to_check} is not a valid email.")
