
import os

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # Be careful with this
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(__file__), 'django.log'),
            'maxBytes': 1024*1024*5,
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
