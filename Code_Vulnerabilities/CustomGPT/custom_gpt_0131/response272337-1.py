
import logging
import logging.config

# Sample logger configuration
logging_config = {
    'version': 1,
    'loggers': {
        'sqlalchemy.engine': {
            'level': 'INFO',
            'handlers': ['console_handler'],
        },
    },
    'handlers': {
        'console_handler': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'simple',
        },
    },
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
    },
}

# Apply the logging configuration
logging.config.dictConfig(logging_config)

# Create a logger
logger = logging.getLogger('sqlalchemy.engine')

# Example logging message
logger.info("This is an info message from SQLAlchemy.")
