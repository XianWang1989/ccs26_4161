
import logging
import logging.config

# Sample configuration as a dictionary
logging_config = {
    'version': 1,
    'loggers': {
        'sqlalchemy.engine': {
            'level': 'INFO',
            'handlers': [],
            'propagate': False,
        },
    },
}

# Configure logging
logging.config.dictConfig(logging_config)

# Example usage
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message.')
