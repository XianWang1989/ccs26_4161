
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
            'filename': os.path.join(BASE_DIR, 'logs', 'django.log'),  # Update file path
            'maxBytes': 1024*1024*5, 
            'formatter': 'standard',
            'backupCount': 5,
            'encoding': 'utf-8',  # Ensure proper encoding
        },
    },
    'loggers': {
        'django': {  # Use 'django' logger to catch all internal logs
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
