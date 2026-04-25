
# yourapp/adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user.is_active = True  # Automatically activate
        super().save_user(request, user, form, commit)

# settings.py
ACCOUNT_ADAPTER = 'yourapp.adapters.MyAccountAdapter'
