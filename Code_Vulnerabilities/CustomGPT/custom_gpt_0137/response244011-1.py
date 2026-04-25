
import logging
import os

LOGGING_DIR = os.path.join(BASE_DIR, 'logs')  # Ensure you're using BASE_DIR or the correct path
if not os.path.exists(LOGGING_DIR):
    os.makedirs(LOGGING_DIR)  # Create logs directory if it doesn't exist

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
            'filename': os.path.join(LOGGING_DIR, 'django.log'),  # Change to use the LOGGING_DIR
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
