
import logging
from django.shortcuts import render
from django.template.context_processors import csrf

# Get an instance of the logger
logr = logging.getLogger('django')

def login(request):
    logr.debug("THIS BETTER WORK >:O")
    c = {}
    c.update(csrf(request))
    return render(request, 'accounts/login.html', c)
