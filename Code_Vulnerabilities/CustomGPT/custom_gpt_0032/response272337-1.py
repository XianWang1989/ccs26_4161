
import logging
import logging.config

# Configuration (usually this could come from a file)
config = {
    'version': 1,
    'loggers': {
        'sqlalchemy.engine': {
            'level': 'INFO',
            'handlers': ['console'],
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
}

# Apply the logging configuration
logging.config.dictConfig(config)

# Example of using the logger
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message.')
