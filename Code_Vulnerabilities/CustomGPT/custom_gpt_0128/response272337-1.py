
import logging
import logging.config

# Example logging configuration as a dictionary
log_config = {
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
            'level': 'DEBUG',
        },
    },
}

# Configure logging
logging.config.dictConfig(log_config)

# Example usage
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message.')
