
import logging
import logging.config

# Sample logging configuration in Python code
logging_config = {
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
            'formatter': 'simple',
        },
    },
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
    },
}

# Configure logging
logging.config.dictConfig(logging_config)

# Using the logger
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an informational message.')
