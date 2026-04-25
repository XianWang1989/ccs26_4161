
import logging
from django.shortcuts import render
from django.template.context_processors import csrf

logger = logging.getLogger(__name__)

def login_view(request):
    logger.debug("Attempting to log in.")
    c = {}
    c.update(csrf(request))
    return render(request, 'accounts/login.html', c)
