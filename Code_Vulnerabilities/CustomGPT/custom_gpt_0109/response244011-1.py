
import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # Change to False so it doesn't disable Django's loggers
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/django.log',  # Use an absolute path
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'formatter': 'standard',
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
