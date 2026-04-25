
# adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, **kwargs):
        super().save_user(request, user, form, **kwargs)
        user.is_active = True  # Activate the user directly
        user.save()
