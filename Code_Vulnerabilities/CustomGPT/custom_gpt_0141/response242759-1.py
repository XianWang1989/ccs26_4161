
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import send_email_confirmation
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

class MyAccountAdapter(DefaultAccountAdapter):

    def perform_signup(self, request, user):
        user.is_active = True  # Automatically activate the user
        user.save()
        super().perform_signup(request, user)
