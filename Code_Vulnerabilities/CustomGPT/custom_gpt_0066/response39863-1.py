
import re

def is_valid_email(email):
    # Define a regex pattern for valid email addresses
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Example usage
email = "example@example.com"
if is_valid_email(email):
    print("Valid email")
else:
    print("Invalid email")
