
import re

def is_valid_email(email):
    # Regular expression for validating an Email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Example usage
email_to_check = 'example@domain.com'
if is_valid_email(email_to_check):
    print(f"{email_to_check} is a valid email.")
else:
    print(f"{email_to_check} is not a valid email.")
