
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
            'filename': os.path.join('/var/log/django', 'django.log'),  # Updated path
            'maxBytes': 1024 * 1024 * 5,
            'formatter': 'standard',
            'backupCount': 5,
        },
    },
    'loggers': {
        '': {  # Root logger
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Ensure the log directory exists and has correct permissions
if not os.path.exists('/var/log/django'):
    os.makedirs('/var/log/django')
    os.chmod('/var/log/django', 0o755)  # Set directory permissions
