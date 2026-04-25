
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import complete_signup

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        # Set the user as active after signup
        sociallogin.is_new = True
        sociallogin.user.is_active = True
        sociallogin.user.save()
