
from allauth.account.utils import complete_signup
from django.http import HttpResponseRedirect
from django.urls import reverse

def custom_signup(request, **kwargs):
    response = complete_signup(request, **kwargs)
    user = request.user
    if user and not user.is_active:
        user.is_active = True
        user.save()
    return response
