
import logging
from django.shortcuts import render
from django.template.context_processors import csrf

logr = logging.getLogger('django')  # Match the logger name defined in LOGGING

def login(request):
    logr.debug("THIS BETTER WORK >:O")
    c = {}
    c.update(csrf(request))
    return render(request, 'accounts/login.html', c)
