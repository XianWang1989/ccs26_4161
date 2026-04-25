
import os
import logging
from django.utils.log import DEFAULT_LOGGING

LOGGING_DIR = os.path.join(BASE_DIR, 'logs')  # Ensure BASE_DIR is defined
if not os.path.exists(LOGGING_DIR):
    os.makedirs(LOGGING_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # Set this to False to avoid disabling existing loggers
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_DIR, 'django.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'myapp': {  # Replace 'myapp' with your app's name
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
