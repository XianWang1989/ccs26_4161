
import logging
from django.shortcuts import render
from django.template.context_processors import csrf

logger = logging.getLogger(__name__)

def login(request):
    logger.debug("Debugging login view.")
    context = {}
    context.update(csrf(request))
    return render(request, 'accounts/login.html', context)
