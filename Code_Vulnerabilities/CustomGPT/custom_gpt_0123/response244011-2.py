
import logging
from django.shortcuts import render
from django.template.context_processors import csrf

logr = logging.getLogger('django')

def login(request):
    logr.debug("Debug message: User attempted to log in.")
    c = {}
    c.update(csrf(request))
    return render(request, 'accounts/login.html', c)
