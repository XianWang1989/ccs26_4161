
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_email, send_email_confirmation
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user.is_active = True  # Automatically activate user
        user.save()
        return super().save_user(request, user, form, commit=commit)
