
# adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def complete_signup(self, request, user, email, **kwargs):
        user.is_active = True
        user.save()
        return super().complete_signup(request, user, email, **kwargs)
