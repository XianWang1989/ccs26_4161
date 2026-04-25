
import logging
import logging.config

# Example of a configuration dictionary
logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        'sqlalchemy.engine': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
}

# Apply the logging configuration
logging.config.dictConfig(logging_config)

# Create a logger
logger = logging.getLogger('sqlalchemy.engine')

# Example usage
logger.info('This is an info message from the SQLAlchemy engine logger.')
