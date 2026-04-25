
import logging
from django.template.context_processors import csrf
from django.shortcuts import render

logr = logging.getLogger(__name__)

def login(request):
    logr.debug("THIS BETTER WORK >:O")
    c = {}
    c.update(csrf(request))
    return render(request, 'accounts/login.html', c)
