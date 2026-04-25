
import logging
from django.template.context_processors import csrf
from django.shortcuts import render

logr = logging.getLogger(__name__)

def login(request):
    try:
        logr.debug("Starting login function")
        c = {}
        c.update(csrf(request))
        logr.debug("CSRF token updated in context")
        return render(request, 'accounts/login.html', c)
    except Exception as e:
        logr.error("Error in login function: %s", e)
