
'handlers': {
    'console': {
        'class': 'logging.StreamHandler',
    },
},
'loggers': {
    '': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propagate': True,
    },
},
