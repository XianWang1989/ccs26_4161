
import os
import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(__file__), 'logs/django.log'),  # Use an absolute path if needed
            'maxBytes': 1024 * 1024 * 5,
            'formatter': 'standard',
            'backupCount': 5,
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Usage in a view
import logging
from django.shortcuts import render
from django.template.context_processors import csrf

logr = logging.getLogger(__name__)

def login(request):
    logr.debug("THIS BETTER WORK!")
    c = {}
    c.update(csrf(request))
    return render(request, 'accounts/login.html', c)
