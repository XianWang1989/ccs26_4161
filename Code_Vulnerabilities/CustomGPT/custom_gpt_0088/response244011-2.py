
import logging
from django.shortcuts import render
from django.template.context_processors import csrf

# Initialize logger
logr = logging.getLogger(__name__)

def login(request):
    logr.debug("THIS BETTER WORK >:O")  # Debug log message
    c = {}
    c.update(csrf(request))
    return render(request, 'accounts/login.html', c)
