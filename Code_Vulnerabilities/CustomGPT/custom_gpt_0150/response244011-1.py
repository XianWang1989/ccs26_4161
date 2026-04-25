
import logging
from django.conf import settings

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # Change this to False
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/path/to/your/logs/django.log',  # Ensure this path is correct
            'maxBytes': 1024 * 1024 * 5,
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

# Don't forget to call this in your WSGI file
if __name__ == "__main__":
    logging.config.dictConfig(LOGGING)
