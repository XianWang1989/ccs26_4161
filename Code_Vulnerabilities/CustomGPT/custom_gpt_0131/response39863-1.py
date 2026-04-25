
import re

def is_valid_email(email):
    # Regular expression for validating an Email
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

# Example usage
email_to_test = "example@example.com"
if is_valid_email(email_to_test):
    print(f"{email_to_test} is a valid email.")
else:
    print(f"{email_to_test} is not a valid email.")
