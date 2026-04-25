
import logging
from django.shortcuts import render
from django.template.context_processors import csrf

logr = logging.getLogger(__name__)

def login(request):
    logr.debug("Entering login view")
    c = {}
    c.update(csrf(request))
    logr.debug("CSRF context updated")
    return render(request, 'accounts/login.html', c)
