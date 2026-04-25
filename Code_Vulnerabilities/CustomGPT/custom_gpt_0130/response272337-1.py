
import logging
import logging.config

# Simulate a config using a dictionary (or you could read it from an actual config file)
config = {
    'version': 1,
    'loggers': {
        'sqlalchemy.engine': {
            'level': 'INFO',
            'handlers': [],  # Add your handlers here
        },
    },
}

logging.config.dictConfig(config)

# Example usage
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message.')
