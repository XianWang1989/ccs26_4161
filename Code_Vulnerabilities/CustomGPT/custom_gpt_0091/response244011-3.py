
'handlers': {
    'console': {
        'class': 'logging.StreamHandler',
    },
    'default': {
        'level': 'DEBUG',
        'class': 'logging.handlers.RotatingFileHandler',
        'filename': os.path.join(BASE_DIR, 'logs', 'django.log'),
        ...
    },
},
'loggers': {
    '': {
        'handlers': ['default', 'console'],  # Add console handler
        'level': 'DEBUG',
        'propagate': True,
    },
},
