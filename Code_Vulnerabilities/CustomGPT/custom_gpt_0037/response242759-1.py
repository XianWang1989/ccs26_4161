
# myapp/adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def is_auto_loss(self, *args, **kwargs):
        return True  # Automatically activates users

    def save_user(self, request, user, form, commit=True):
        user.is_active = True  # Set user to active
        return super().save_user(request, user, form, commit)
