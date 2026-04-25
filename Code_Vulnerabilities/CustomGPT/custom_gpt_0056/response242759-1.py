
# myapp/adapters.py

from allauth.account.adapter import DefaultAccountAdapter
from django.utils.translation import gettext_lazy as _

class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, **kwargs):
        super().save_user(request, user, form, **kwargs)
        # Auto-activate user
        user.is_active = True
        user.save()
