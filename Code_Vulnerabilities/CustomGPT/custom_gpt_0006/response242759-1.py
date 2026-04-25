
# adapters.py

from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import complete_signup

class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, **kwargs):
        user.is_active = True  # Automatically activate user
        super().save_user(request, user, form, **kwargs)
