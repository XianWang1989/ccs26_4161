
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import send_email_confirmation

class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user.is_active = True  # Automatically activate the user
        user.save()
        return user
