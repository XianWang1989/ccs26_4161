
import logging
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf

# Configure logger
logger = logging.getLogger(__name__)

def login(request):
    # Test logging
    logger.debug("This is a debug message.")

    c = {}
    c.update(csrf(request))
    return render(request, 'accounts/login.html', c)
