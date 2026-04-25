
import logging
import logging.config

# Example configuration as a dictionary
logging_config = {
    'version': 1,
    'loggers': {
        'sqlalchemy.engine': {
            'level': 'INFO',
            'handlers': ['console'],  # Assuming there's a handler defined
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        }
    },
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        }
    }
}

# Apply the logging configuration
logging.config.dictConfig(logging_config)

# Example usage
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message')
