
'handlers': {
    'console': {
        'class': 'logging.StreamHandler',
    },
    'default': {
        'level': 'DEBUG',
        'class': 'logging.handlers.RotatingFileHandler',
        'filename': os.path.join(LOGGING_DIR, 'django.log'),
        'maxBytes': 1024 * 1024 * 5,
        'backupCount': 5,
        'formatter': 'standard',
    },
},
'loggers': {
    'django': {
        'handlers': ['default', 'console'],  # Add 'console' here
        'level': 'DEBUG',
        'propagate': True,
    },
},
