
# adapters.py
from allauth.account.adapter import get_adapter
from allauth.account.utils import complete_signup
from django.utils.http import url_has_allowed_host_and_scheme

class CustomAccountAdapter(DefaultAccountAdapter):

    def perform_signup(self, request, user):
        user.is_active = True  # Automatically activate the user
        user.save()
        return super().perform_signup(request, user)

# settings.py
ACCOUNT_ADAPTER = 'yourapp.adapters.CustomAccountAdapter'
