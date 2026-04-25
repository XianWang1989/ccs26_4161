
import logging
from django.shortcuts import render
from django.template.context_processors import csrf

logr = logging.getLogger(__name__)

def login(request):
    logr.debug("THIS BETTER WORK &gt;:O")
    context = {}
    context.update(csrf(request))
    return render(request, 'accounts/login.html', context)
