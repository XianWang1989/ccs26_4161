
import os
import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join('/logs', 'django.log'),  # Ensure this path is correct
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {  # Log only Django-specific messages
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        '': {  # Catch all other logs
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
