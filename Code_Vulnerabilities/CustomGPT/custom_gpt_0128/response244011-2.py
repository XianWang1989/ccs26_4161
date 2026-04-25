
import logging
from django.shortcuts import render
from django.middleware.csrf import get_token

logr = logging.getLogger(__name__)

def login(request):
    logr.debug("THIS BETTER WORK >:O")
    c = {}
    get_token(request)  # Updated for CSRF usage
    return render(request, 'accounts/login.html', c)
