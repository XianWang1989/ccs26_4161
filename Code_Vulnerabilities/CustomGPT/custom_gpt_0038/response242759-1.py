
# adapters.py

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import complete_signup
from django.utils.translation import gettext as _
from allauth.account.utils import send_email_confirmation
from django.utils import timezone

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user
        user.is_active = True  # Automatically activate user
        user.save()

        # Send confirmation email if needed
        if user.email and user.email not in [email.email for email in user.emailaddress_set.all()]:
            send_email_confirmation(request, user)

