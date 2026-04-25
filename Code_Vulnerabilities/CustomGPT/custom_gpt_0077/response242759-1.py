
# adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return True

    def save_user(self, request, user, form, **kwargs):
        # Automatically activate the user
        user.is_active = True
        super().save_user(request, user, form, **kwargs)
