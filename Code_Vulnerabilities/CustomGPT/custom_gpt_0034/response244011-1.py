
import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # Change to False for better debugging
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/logs/django.log',
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

# Log to confirm logging configuration
logging.basicConfig(level=logging.DEBUG)
logr = logging.getLogger(__name__)
logr.info("Logging is configured!")

def login(request):
    logr.debug("THIS BETTER WORK >:O")
    c = {}
    c.update(csrf(request))
    return render_to_response('accounts/login.html', c)
