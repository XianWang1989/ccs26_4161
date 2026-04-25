
import logging
import os

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # Changed to False for better control
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'django.log'),  # Use an absolute path
            'maxBytes': 1024 * 1024 * 5,
            'formatter': 'standard',
            'backupCount': 5,
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'error.log'),  # Additional error log
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['default', 'error'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
