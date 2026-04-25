
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
            'filename': os.path.join('/var/log', 'django.log'),  # Use absolute path
            'maxBytes': 1024 * 1024 * 5,
            'formatter': 'standard',
            'backupCount': 5,
        },
    },
    'loggers': {
        'django': {  # Specifically log for Django
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False,
        },
        '': {  # Default logger for other usage
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
