
import logging
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

logr = logging.getLogger(__name__)

@csrf_exempt
def login(request):
    logr.debug("THIS BETTER WORK >:O")
    c = {}
    c.update(csrf(request))
    return render(request, 'accounts/login.html', c)
