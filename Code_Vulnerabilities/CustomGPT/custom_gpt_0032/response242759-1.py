
# yourapp/adapters.py
from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, **kwargs):
        # Call the original save_user method
        super().save_user(request, user, form, **kwargs)
        # Automatically activate the user
        user.is_active = True
        user.save()
