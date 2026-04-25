
import os
import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # Change to False to avoid disabling other loggers
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/django.log',  # Ensure this path is correct
            'maxBytes': 1024 * 1024 * 5,
            'formatter': 'standard',
            'backupCount': 5,
        },
    },
    'loggers': {
        'django': {  # Use 'django' logger to capture Django's log messages
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'myapp': {  # Replace 'myapp' with your app name
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
