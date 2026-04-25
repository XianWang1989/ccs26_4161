
from allauth.account.signals import user_signed_up
from allauth.account.models import EmailAddress
from django.dispatch import receiver

@receiver(user_signed_up)
def activate_user(sender, request, user, **kwargs):
    user.is_active = True
    user.save()
    EmailAddress.objects.create(user=user, email=user.email, primary=True, verified=True)
