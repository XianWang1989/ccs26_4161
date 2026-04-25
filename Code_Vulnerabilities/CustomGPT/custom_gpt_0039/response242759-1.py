
# adapters.py
from allauth.account.adapter import DefaultAccountAdapter
from django.utils.translation import gettext_lazy as _

class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user.is_active = True  # Activate the user
        user.save()
        return super().save_user(request, user, form, commit=commit)
