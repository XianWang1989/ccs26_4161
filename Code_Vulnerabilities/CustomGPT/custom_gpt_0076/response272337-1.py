
import logging
import logging.config

# Example logging configuration using a dictionary
logging_config = {
    'version': 1,
    'loggers': {
        'sqlalchemy.engine': {
            'level': 'INFO',
            'handlers': [],
        }
    },
}

logging.config.dictConfig(logging_config)

# Usage example
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message.')
