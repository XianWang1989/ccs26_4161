
# yourapp/adapters.py

from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def perform_create(self, request, *args, **kwargs):
        user = super().perform_create(request, *args, **kwargs)
        user.is_active = True  # Activate the user
        user.save()
        return user
