
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def is_email_verified(self):
        return True  # Automatically mark the email as verified
