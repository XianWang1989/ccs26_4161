
import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format' : '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/path/to/your/logs/django.log',  # Ensure this is the correct path
            'maxBytes': 1024 * 1024 * 5,
            'formatter' : 'standard',
            'backupCount': 5,
        },
    },
    'loggers': {
        'django': {  # It's good to specifically isolate the Django logger
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
