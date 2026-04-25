
import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # Set this to False to avoid issues with existing loggers
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/django/django.log',
            'maxBytes': 1024 * 1024 * 5,
            'formatter': 'standard',
            'backupCount': 5,
        },
    },
    'loggers': {
        'django': {  # Specific logger for django
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
