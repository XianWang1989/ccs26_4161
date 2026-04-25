
import logging
from django.shortcuts import render
from django.template.context_processors import csrf

# Configure your logger
logr = logging.getLogger(__name__)

def login(request):
    logr.debug("THIS BETTER WORK >:O")  # Log the debug message
    c = {}
    c.update(csrf(request))
    return render(request, 'accounts/login.html', c)
