
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
            'filename': os.path.join('/var/log/django', 'django.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5MB
            'formatter': 'standard',
            'backupCount': 5,
        },
    },
    'loggers': {
        'django': {  # Use 'django' for Django-specific logging
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        },
        '': {  # Root logger
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
