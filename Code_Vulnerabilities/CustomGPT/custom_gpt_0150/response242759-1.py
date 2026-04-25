
# adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return True  # Allow signup

    def save_user(self, request, user, form, **kwargs):
        super().save_user(request, user, form, **kwargs)
        user.is_active = True  # Activate the user
        user.save()
