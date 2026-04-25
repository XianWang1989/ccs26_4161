
# yourapp/adapters.py
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user.is_active = True  # Activate the user
        super(MyAccountAdapter, self).save_user(request, user, form, commit)
