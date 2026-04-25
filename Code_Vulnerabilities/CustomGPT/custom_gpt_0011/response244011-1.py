
import os
import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # Set to False to avoid disabling default loggers
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join('/path/to/your/logs', 'django.log'),  # Use absolute path
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
