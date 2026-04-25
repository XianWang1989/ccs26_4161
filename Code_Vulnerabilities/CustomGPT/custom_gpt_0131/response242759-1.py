
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, **kwargs):
        super(MyAccountAdapter, self).save_user(request, user, form, **kwargs)
        user.is_active = True  # Automatically activate the user
        user.save()
