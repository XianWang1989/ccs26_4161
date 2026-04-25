
import logging
from django.shortcuts import render
from django.template.context_processors import csrf

log = logging.getLogger(__name__)

def login(request):
    log.debug("THIS BETTER WORK >:O")
    context = {}
    context.update(csrf(request))
    return render(request, 'accounts/login.html', context)
