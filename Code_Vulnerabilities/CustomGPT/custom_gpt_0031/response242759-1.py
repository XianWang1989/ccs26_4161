
# forms.py
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import complete_signup

class CustomSignupAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, **kwargs):
        user.is_active = True  # Automatically activate the user
        user.save()
        complete_signup(request, user, self.get_success_url(request, user))

# settings.py
ACCOUNT_ADAPTER = 'yourapp.forms.CustomSignupAdapter'
