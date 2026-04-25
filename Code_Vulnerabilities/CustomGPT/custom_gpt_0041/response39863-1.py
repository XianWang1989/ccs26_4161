
import re

def is_valid_email(email):
    # Regular expression for validating an Email
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

# Example usage
email_to_test = "example@example.com"
if is_valid_email(email_to_test):
    print("Valid email address.")
else:
    print("Invalid email address.")
