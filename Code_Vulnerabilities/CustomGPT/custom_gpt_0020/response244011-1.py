
import os
import logging

# Configure the logs directory in relation to your project
LOG_DIR = os.path.join(BASE_DIR, 'logs')
os.makedirs(LOG_DIR, exist_ok=True)  # Create the logs directory if it doesn't exist

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # Set to False to avoid disabling existing loggers
    'formatters': {
        'standard': {
            'format' : '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'django.log'),  # Use the correct path
            'maxBytes': 1024*1024*5,
            'formatter' : 'standard',
            'backupCount': 5,
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
