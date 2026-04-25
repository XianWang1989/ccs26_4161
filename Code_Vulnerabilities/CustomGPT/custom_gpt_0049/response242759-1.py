
# signals.py
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

@receiver(user_signed_up)
def user_signed_up_override(request, user, **kwargs):
    user.is_active = True  # Automatically activate the user
    user.save()
