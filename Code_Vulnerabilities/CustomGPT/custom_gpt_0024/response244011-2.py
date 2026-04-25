
import logging
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.shortcuts import render

# Get the logger
logr = logging.getLogger(__name__)

def login(request):
    logr.debug("THIS BETTER WORK >:O")
    c = {}
    c.update(csrf(request))
    return render(request, 'accounts/login.html', c)
