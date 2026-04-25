
import logging
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render

logr = logging.getLogger('django')  # Match the logger name

@csrf_protect
def login(request):
    logr.debug("THIS BETTER WORK >:O")
    c = {}
    return render(request, 'accounts/login.html', c)  # Use render instead of render_to_response
