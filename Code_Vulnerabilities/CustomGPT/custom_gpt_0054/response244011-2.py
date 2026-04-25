
'handlers': {
    'console': {
        'class': 'logging.StreamHandler',
    },
    'default': {
        'level': 'DEBUG',
        'class': 'logging.handlers.RotatingFileHandler',
        'filename': 'logs/django.log',  # Make sure this is a correct relative path
        'maxBytes': 1024*1024*5,
        'formatter': 'standard',
        'backupCount': 5,
    },
},
'loggers': {
    'django': {
        'handlers': ['console', 'default'],
        'level': 'DEBUG',
        'propagate': True,
    },
},
