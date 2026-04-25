
from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return True

    def save_user(self, request, user, form, commit=True):
        user.is_active = True  # Automatically activate user
        return super().save_user(request, user, form, commit)

# In your settings.py
ACCOUNT_ADAPTER = 'path.to.your.CustomAccountAdapter'
