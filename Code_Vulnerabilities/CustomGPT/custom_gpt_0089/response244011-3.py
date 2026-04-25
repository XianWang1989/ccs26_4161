
import logging
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

logr = logging.getLogger(__name__)

@csrf_protect
def login(request):
    logr.debug("Logging in user")
    c = {}
    c.update(csrf(request))
    return render(request, 'accounts/login.html', c)
