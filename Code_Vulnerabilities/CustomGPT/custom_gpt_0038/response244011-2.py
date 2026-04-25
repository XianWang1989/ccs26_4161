
import logging
from django.shortcuts import render
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect

logr = logging.getLogger('django')

@csrf_protect
def login(request):
    logr.debug("This is a debug message.")
    context = {}
    return render(request, 'accounts/login.html', context)
