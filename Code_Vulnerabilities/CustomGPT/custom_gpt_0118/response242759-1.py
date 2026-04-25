
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import complete_signup
from allauth.account.signals import user_signed_up

class MyAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return True  # Allow signup

@receiver(user_signed_up)
def activate_user(sender, request, user, **kwargs):
    user.is_active = True
    user.save()
