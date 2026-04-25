
# adapters.py
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import complete_signup

class MyAccountAdapter(DefaultAccountAdapter):
    def send_confirmation_mail(self, request, emailconfirmation):
        # Skip sending confirmation email
        pass

    def save_user(self, request, user, form, commit=True):
        user.is_active = True  # Automatically activate user
        return super().save_user(request, user, form, commit)
