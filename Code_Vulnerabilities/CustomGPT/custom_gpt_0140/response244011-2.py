
import logging
from django.shortcuts import render

logr = logging.getLogger(__name__)

def login(request):
    logr.debug("THIS BETTER WORK &gt;:O")
    c = {}
    c.update(csrf(request))
    return render(request, 'accounts/login.html', c)
