
import logging
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

logr = logging.getLogger(__name__)

@csrf_exempt
def login(request):
    logr.debug("Debugging login view")
    # Your authentication logic here...
    c = {}
    return render(request, 'accounts/login.html', c)
