
import logging
from django.conf import settings
from django.shortcuts import render
from django.middleware.csrf import get_token

# Logger configuration
logger = logging.getLogger(__name__)

def login(request):
    logger.debug("Debugging the login function.")
    c = {}
    get_token(request)  # Update CSRF token
    return render(request, 'accounts/login.html', c)
