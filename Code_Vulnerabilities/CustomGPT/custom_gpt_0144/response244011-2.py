from cloghandler import ConcurrentRotatingFileHandler

'handlers': {
    'file': {
        'level': 'DEBUG',
        'class': 'cloghandler.ConcurrentRotatingFileHandler',
        'filename': '/var/log/django/django.log',
        'maxBytes': 1024*1024*5,
        'backupCount': 5,
        'formatter': 'standard',
    },
},
