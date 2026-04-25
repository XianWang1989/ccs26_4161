
# apps.py or signals.py

from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(user_signed_up)
def automatically_activate_user(request, user, **kwargs):
    user.is_active = True
    user.save()
