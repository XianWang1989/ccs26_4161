
# adapters.py
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import send_email_confirmation

class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, **kwargs):
        super().save_user(request, user, form, **kwargs)
        user.is_active = True  # Automatically activate user
        user.save()

# settings.py
ACCOUNT_ADAPTER = 'yourapp.adapters.MyAccountAdapter'
