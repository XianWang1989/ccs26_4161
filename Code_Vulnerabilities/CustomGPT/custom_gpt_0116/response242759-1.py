
# myapp/adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return True  # Allow all signups

    def save_user(self, request, user, form, commit=True):
        user.is_active = True  # Activate the user immediately
        user.save()
        return super().save_user(request, user, form, commit)
