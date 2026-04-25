
# myapp/adapters.py

from allauth.account.adapter import DefaultAccountAdapter
from django.utils import timezone

class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user.is_active = True  # Automatically activate user
        user.date_joined = timezone.now()
        user.save()
        return user
