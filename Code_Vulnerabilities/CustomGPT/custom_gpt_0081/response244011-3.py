
import logging
from django.shortcuts import render
from django.middleware.csrf import get_token

logger = logging.getLogger(__name__)

def login(request):
    logger.debug("Debug message from login view")
    c = {}
    c['csrf_token'] = get_token(request)
    return render(request, 'accounts/login.html', c)
