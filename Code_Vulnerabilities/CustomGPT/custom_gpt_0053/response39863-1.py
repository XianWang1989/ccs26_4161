
import re

def is_valid_email(email):
    # Define a regex pattern for validating email addresses
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Test the function
emails_to_test = [
    "test@example.com",
    "invalid-email",
    "user@domain.co",
    "user@.com"
]

for email in emails_to_test:
    if is_valid_email(email):
        print(f"{email} is valid.")
    else:
        print(f"{email} is invalid.")
