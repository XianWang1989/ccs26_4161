
import logging
from django.shortcuts import render
from django.template.context_processors import csrf

logr = logging.getLogger(__name__)

def login(request):
    logr.debug("THIS BETTER WORK >:O")
    c = {}
    c.update(csrf(request))  # Update context with CSRF token
    return render(request, 'accounts/login.html', c)  # Use render() instead of render_to_response()
