
import logging
from django.shortcuts import render
from django.template.context_processors import csrf

logr = logging.getLogger(__name__)

def login(request):
    logr.debug("Debugging the login view")
    c = {}
    c.update(csrf(request))
    return render(request, 'accounts/login.html', c)
