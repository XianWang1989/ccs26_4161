# signals.py
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.shortcuts import redirect

@receiver(user_signed_up)
def after_signup(sender, request, user, **kwargs):
    if user.profile.user_type == 'architect':
        request.session['post_signup_redirect'] = '/extra-architect-form/'
