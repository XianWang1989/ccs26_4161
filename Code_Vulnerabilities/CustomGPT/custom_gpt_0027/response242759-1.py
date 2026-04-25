
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def is_auto_activate(self, request, **kwargs):
        return True  # Automatically activate users

# Then add this to your settings.py
ACCOUNT_ADAPTER = 'yourapp.adapters.MyAccountAdapter'
