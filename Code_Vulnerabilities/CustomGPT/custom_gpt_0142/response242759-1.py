
# adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def new_user(self):
        user = super().new_user()
        user.is_active = True  # Automatically activate the user
        user.save()
        return user
