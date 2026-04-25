
# adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        super().save_user(request, user, form, commit)
        user.is_active = True  # Automatically activate the user
        if commit:
            user.save()
