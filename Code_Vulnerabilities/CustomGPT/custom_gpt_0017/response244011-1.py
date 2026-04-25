
import logging
from django.conf import settings
from django.shortcuts import render
from django.template.context_processors import csrf
from django.http import HttpRequest

# Configure logging in settings.py
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
            'filename': '/var/log/myproject/django.log',  # Change to an absolute path
            'maxBytes': 1024 * 1024 * 5,
            'formatter': 'standard',
            'backupCount': 5,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# In your views.py
logger = logging.getLogger(__name__)

def login(request: HttpRequest):
    logger.debug("THIS BETTER WORK &gt;:O")
    context = {}
    context.update(csrf(request))
    return render(request, 'accounts/login.html', context)
