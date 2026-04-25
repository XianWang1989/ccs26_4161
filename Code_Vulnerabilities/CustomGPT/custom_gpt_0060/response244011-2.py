
import logging
from django.shortcuts import render
from django.template.context_processors import csrf

logr = logging.getLogger(__name__)

def login(request):
    logr.debug("Entering the login view.")
    c = {}
    c.update(csrf(request))

    logr.debug("CSRF token added to context.")
    return render(request, 'accounts/login.html', c)
