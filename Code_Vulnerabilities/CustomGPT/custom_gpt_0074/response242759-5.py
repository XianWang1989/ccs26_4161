
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.shortcuts import redirect

@receiver(user_signed_up)
def user_signed_up_handler(request, user, **kwargs):
    if user.user_type == 'architect':
        return redirect('business_details')  # Replace with your business details URL
