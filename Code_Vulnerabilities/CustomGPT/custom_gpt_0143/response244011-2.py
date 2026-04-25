
# views.py
import logging
from django.shortcuts import render
from django.template.context_processors import csrf

log = logging.getLogger(__name__)

def login(request):
    log.debug("Debug message: User accessed login view.")
    c = {}
    c.update(csrf(request))
    return render(request, 'accounts/login.html', c)
