
import logging
import os

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
            'filename': os.path.join('/', 'logs', 'django.log'),  # Check this path properly exists!
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
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

# Example logging outside a view
logger = logging.getLogger(__name__)
logger.debug("Logging is set up!")
