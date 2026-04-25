
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def is_valid_email(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

# Example usage
email_to_check = "example@example.com"
if is_valid_email(email_to_check):
    print(f"{email_to_check} is valid.")
else:
    print(f"{email_to_check} is not valid.")
