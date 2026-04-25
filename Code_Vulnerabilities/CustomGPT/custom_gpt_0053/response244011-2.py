
import logging
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render

log = logging.getLogger(__name__)

@csrf_protect
def login(request):
    log.debug("Trying to log in")
    c = {}
    c.update(csrf(request))
    return render(request, 'accounts/login.html', c)
