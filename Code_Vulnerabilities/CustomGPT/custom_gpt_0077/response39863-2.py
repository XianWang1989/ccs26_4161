
from email_validator import validate_email, EmailNotValidError

def check_email(email):
    try:
        # Validate the email
        validated_email = validate_email(email)
        print(f"Valid email: {validated_email['email']}")
    except EmailNotValidError as e:
        print(str(e))

# Example usage
check_email("test@example.com")
