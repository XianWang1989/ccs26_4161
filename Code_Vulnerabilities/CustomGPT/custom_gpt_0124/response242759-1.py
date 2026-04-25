
# adapters.py
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import complete_signup

class MyAccountAdapter(DefaultAccountAdapter):
    def send_confirmation_email(self, request, user):
        # Override this method to automatically activate user
        user.is_active = True
        user.save()
