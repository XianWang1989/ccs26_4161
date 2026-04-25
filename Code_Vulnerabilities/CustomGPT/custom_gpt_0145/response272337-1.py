
import logging
import logging.config

# Imagine this is your configuration loaded from an INI file
logging_config = {
    'version': 1,
    'loggers': {
        'sqlalchemy.engine': {
            'level': 'INFO',
            'handlers': [],
        },
    },
}

# Configure logging
logging.config.dictConfig(logging_config)

# Example usage
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message from SQLAlchemy engine.')
