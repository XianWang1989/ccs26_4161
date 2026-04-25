
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import complete_signup

class MyAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return True

    def save_user(self, request, user, form, commit=True):
        user.is_active = True  # Automatically activate the user
        user.save()
        return user
