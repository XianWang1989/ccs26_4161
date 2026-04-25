
# adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def complete_signup(self, request, user, response, *args, **kwargs):
        user.is_active = True
        user.save()
        return super().complete_signup(request, user, response, *args, **kwargs)
