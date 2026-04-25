
# adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def complete_signup(self, request, user, sociallogin, **kwargs):
        user.is_active = True  # Activate the user
        user.save()
        super().complete_signup(request, user, sociallogin, **kwargs)
