
import logging
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf

# Get the logger instance
logr = logging.getLogger(__name__)

def login(request):
    logr.debug("THIS BETTER WORK >:O")

    c = {}
    c.update(csrf(request))

    # Return a response (ensure this only renders, not just a response for a login)
    return render(request, 'accounts/login.html', c)
