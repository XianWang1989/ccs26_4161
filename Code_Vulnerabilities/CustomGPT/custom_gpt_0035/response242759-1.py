
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=False)  # Create user without saving
        user.is_active = True  # Activate user
        user.save()  # Save user
        return user
