
# in your_app/adapters.py

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.utils import timezone

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user
        user.is_active = True  # Automatically activate the user
        user.save()
