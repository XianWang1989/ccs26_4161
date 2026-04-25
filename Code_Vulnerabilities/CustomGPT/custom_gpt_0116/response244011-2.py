
import logging
from django.shortcuts import render
from django.template.context_processors import csrf

logger = logging.getLogger('django')

def login(request):
    logger.debug("THIS BETTER WORK >:O")
    c = {}
    c.update(csrf(request))
    return render(request, 'accounts/login.html', c)
