
import os
import logging

# Build the path to the log file
log_file_path = os.path.join(BASE_DIR, 'logs', 'django.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # Set to False to avoid disabling existing loggers
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': log_file_path,  # Use absolute path for log file
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'formatter': 'standard',
            'backupCount': 5,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
