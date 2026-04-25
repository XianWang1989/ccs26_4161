
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import complete_signup

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user.is_active = True  # Activate the user immediately
        super().save_user(request, user, form, commit)

# In settings.py
ACCOUNT_ADAPTER = 'yourapp.adapters.CustomAccountAdapter'
