
# adapters.py
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import complete_signup
from django.utils.translation import gettext as _

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def social_signup(self, request, sociallogin):
        user = sociallogin.save(request)
        user.is_active = True  # Automatically activate user
        user.save()
        complete_signup(request, user, '/')

# Don't forget to specify your adapter in settings.py
ACCOUNT_ADAPTER = 'yourapp.adapters.MySocialAccountAdapter'
