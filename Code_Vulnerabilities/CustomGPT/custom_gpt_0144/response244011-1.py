import logging
import os

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # Retain the default loggers
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/django/django.log',  # Absolute path
            'maxBytes': 1024*1024*5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'root': {  # Root logger
        'handlers': ['file'],
        'level': 'DEBUG',
    },
}
