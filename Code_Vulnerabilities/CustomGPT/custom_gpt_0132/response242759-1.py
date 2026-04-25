
# your_app/adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return True  # Allow all signups

    def save_user(self, request, user, form):
        super().save_user(request, user, form)
        user.is_active = True  # Automatically activate the user
        user.save()
