
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import complete_signup
from django.utils import timezone
from django.contrib.auth import get_user_model

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        user.is_active = True  # Automatically activate the user
        user.save()
        return user
