
import re

def is_valid_email(email):
    # Basic email validation regex
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Example usage
email_to_check = 'example@example.com'
if is_valid_email(email_to_check):
    print(f'The email "{email_to_check}" is valid.')
else:
    print(f'The email "{email_to_check}" is invalid.')
