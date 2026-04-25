
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def check_email(email):
    try:
        validate_email(email)  # This will check if the email is valid
        print(f"{email} is a valid email address.")
    except ValidationError:
        print(f"{email} is not a valid email address.")

# Example usage
email = "example@example.com"
check_email(email)
