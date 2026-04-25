
# adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def send_confirmation_mail(self, request, user):
        # Automatically activate the user
        user.is_active = True
        user.save()
