
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user.is_active = True  # Automatically activate the user
        super(MyAccountAdapter, self).save_user(request, user, form, commit)
