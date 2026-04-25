
# adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def is_active(self, user):
        user.is_active = True  # Automatically activate user
        user.save()
        return True
