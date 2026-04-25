
# adapters.py
from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import get_user_model

class MyAccountAdapter(DefaultAccountAdapter):
    def send_email_confirmation(self, request, emailconfirmation):
        # Automatically activate the user
        emailconfirmation.confirm(self)

# In your settings.py
ACCOUNT_ADAPTER = 'yourapp.adapters.MyAccountAdapter'
