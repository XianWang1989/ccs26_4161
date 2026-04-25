
# signals.py
from allauth.socialaccount.signals import social_account_added
from django.dispatch import receiver
from django.contrib.auth import get_user_model

@receiver(social_account_added)
def activate_user(sender, request, sociallogin, **kwargs):
    user = sociallogin.user
    user.is_active = True
    user.save()
