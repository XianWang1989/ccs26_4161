
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import send_email_confirmation
from django.utils.translation import ugettext_lazy as _

class MyAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return True

    def save_user(self, request, user, form, commit=True):
        user.is_active = True  # Activate user
        user.save()
        return super().save_user(request, user, form, commit)
