
import re

def is_valid_email(email):
    # Regular expression for validating an Email
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(regex, email):
        return True
    else:
        return False

# Example usage
email_to_test = "example@domain.com"
if is_valid_email(email_to_test):
    print(f"{email_to_test} is a valid email address.")
else:
    print(f"{email_to_test} is not a valid email address.")
