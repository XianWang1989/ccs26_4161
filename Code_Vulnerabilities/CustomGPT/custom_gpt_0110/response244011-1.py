
# settings.py

import os
import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # Set to False for additional loggers to work
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join('/logs', 'django.log'),  # Use os.path.join for better path handling
            'maxBytes': 1024 * 1024 * 5,
            'formatter': 'standard',
            'backupCount': 5,
        },
    },
    'loggers': {
        'django': {  # Naming your logger can help in filtering logs
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
