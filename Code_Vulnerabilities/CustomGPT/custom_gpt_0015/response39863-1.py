
import re

def is_valid_email(email):
    # Define a regular expression for validating an Email
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_regex, email):
        return True
    return False

# Example usage
email_to_check = "example@example.com"
if is_valid_email(email_to_check):
    print(f"{email_to_check} is a valid email.")
else:
    print(f"{email_to_check} is not a valid email.")
