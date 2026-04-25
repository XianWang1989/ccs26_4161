
import logging
from django.shortcuts import render
from django.template.context_processors import csrf

logr = logging.getLogger('django')  # Use the defined Django logger

def login(request):
    logr.debug("Login view accessed.")
    c = {}
    c.update(csrf(request))
    return render(request, 'accounts/login.html', c)
