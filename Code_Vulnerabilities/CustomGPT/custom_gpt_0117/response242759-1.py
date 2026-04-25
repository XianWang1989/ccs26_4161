
# adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        super().save_user(request, user, form, commit)
        # Activate the user immediately
        user.is_active = True
        user.save()
