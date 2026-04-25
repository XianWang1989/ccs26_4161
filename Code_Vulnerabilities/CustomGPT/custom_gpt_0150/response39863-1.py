
import re

def is_valid_email(email):
    # Simple regex pattern for validating an email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Example usage
email_to_test = "example@test.com"
if is_valid_email(email_to_test):
    print("Valid email address.")
else:
    print("Invalid email address.")
