
# settings.py

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
            'filename': os.path.join(BASE_DIR, 'logs', 'django.log'),  # Use BASE_DIR for absolute path
            'maxBytes': 1024 * 1024 * 5,
            'formatter': 'standard',
            'backupCount': 5,
        },
    },
    'loggers': {
        'django': {  # You may specify 'django' to filter only Django logs
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False,
        },
        '': {  # Root logger
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
