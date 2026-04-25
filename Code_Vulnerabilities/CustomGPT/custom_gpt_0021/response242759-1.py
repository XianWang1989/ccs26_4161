
# adapters.py
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import complete_signup
from django.utils.translation import gettext as _

class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user = super(MyAccountAdapter, self).save_user(request, user, form, commit)
        user.is_active = True  # Automatically activate the user
        user.save()
        return user
