
# adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return True  # Allow all users to sign up

    def send_confirmation_mail(self, request, emailaddress):
        # Override this method if you don't want to send confirmation emails
        pass
