
# views.py
import logging
from django.shortcuts import render
from django.template.context_processors import csrf

logr = logging.getLogger(__name__)

def login(request):
    logr.debug("THIS BETTER WORK >:O")

    # Test logging with another level
    logr.warning("Warning: This is a test log!")

    c = {}
    c.update(csrf(request))
    return render(request, 'accounts/login.html', c)
