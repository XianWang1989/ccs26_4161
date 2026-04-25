
from pyramid.config import Configurator
import logging.config

# Example INI-like configuration loaded from a file or set as a string
config_dict = {
    'version': 1,
    'loggers': {
        'sqlalchemy.engine': {
            'level': 'INFO',
            'handlers': ['console'],
            'qualname': 'sqlalchemy.engine',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'generic',
        },
    },
    'formatters': {
        'generic': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
    },
}

# Configuring the logging
logging.config.dictConfig(config_dict)
