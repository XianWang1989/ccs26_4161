
import os
import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # Set this to False for better debug info
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join('/logs', 'django.log'),  # Use os.path for compatibility
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {  # Log from Django
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'your_app_name': {  # Replace with your app's name for specific logging
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
