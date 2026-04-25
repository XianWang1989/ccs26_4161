
# views.py

import logging
from django.shortcuts import render
from django.template.context_processors import csrf

# Create logger
logr = logging.getLogger('django')  # Use the same name as in LOGGING config

def login(request):
    logr.debug("DEBUG: Attempting to log in")  # Sample log message
    c = {}
    c.update(csrf(request))
    return render(request, 'accounts/login.html', c)
