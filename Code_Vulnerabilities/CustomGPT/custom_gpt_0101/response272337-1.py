
import logging.config

# Example configuration dictionary equivalent to the INI format
config = {
    'loggers': {
        'sqlalchemy.engine': {
            'level': 'INFO',
            'handlers': []
        }
    }
}

# Set up logging
logging.config.dictConfig(config)

# Example usage
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message.')
