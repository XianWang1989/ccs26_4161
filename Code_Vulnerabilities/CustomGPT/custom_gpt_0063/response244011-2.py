
import logging
from django.shortcuts import render
from django.template.context_processors import csrf

logr = logging.getLogger(__name__)

def login(request):
    logr.debug("Debug message: THIS BETTER WORK >:O")
    c = {}
    c.update(csrf(request))
    return render(request, 'accounts/login.html', c)  # Updated render method
