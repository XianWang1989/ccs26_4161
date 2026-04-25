
import logging
from django.shortcuts import render
from django.template.context_processors import csrf

logger = logging.getLogger('myapp')  # Match the app name with the logger defined

def login(request):
    logger.debug("THIS BETTER WORK >:O")
    context = {}
    context.update(csrf(request))
    return render(request, 'accounts/login.html', context)
