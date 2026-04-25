
from email_validator import validate_email, EmailNotValidError

def validate_email_address(email):
    try:
        # Validate and get info
        valid = validate_email(email)
        return valid.email  # This is the normalized email
    except EmailNotValidError as e:
        # Email is not valid, exception message is human-readable
        print(str(e))
        return None

# Example usage
email = "example@domain.com"
if validate_email_address(email):
    print("Valid email.")
else:
    print("Invalid email.")
