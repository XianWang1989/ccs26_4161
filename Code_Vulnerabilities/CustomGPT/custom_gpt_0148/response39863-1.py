
import re

def is_valid_email(email):
    pattern = r"[^@]+@[^@]+\.[^@]+"
    return re.match(pattern, email) is not None

# Example usage
email = "example@example.com"
if is_valid_email(email):
    print("Valid email")
else:
    print("Invalid email")
