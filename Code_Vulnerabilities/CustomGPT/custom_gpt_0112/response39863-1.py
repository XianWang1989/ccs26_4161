
import re

def is_valid_email(email):
    # Regular expression for validating an Email
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

# Example usage
email = "example@domain.com"
if is_valid_email(email):
    print(f"{email} is valid.")
else:
    print(f"{email} is not valid.")
