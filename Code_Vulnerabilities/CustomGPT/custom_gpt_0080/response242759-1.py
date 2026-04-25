
# adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def complete_signup(self, request, user, options):
        user.is_active = True  # Activate user
        user.save()
        return super().complete_signup(request, user, options)
