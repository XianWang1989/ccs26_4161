
import logging
from django.shortcuts import render
from django.middleware.csrf import get_token

logr = logging.getLogger(__name__)

def login(request):
    logr.debug("Login function called")
    c = {}
    c['csrf_token'] = get_token(request)
    return render(request, 'accounts/login.html', c)
