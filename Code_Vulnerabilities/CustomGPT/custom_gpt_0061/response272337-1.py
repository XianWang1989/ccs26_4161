
import logging
import logging.config

# Configuration dictionary mimicking your INI-like format
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

# Apply logging configuration
logging.config.dictConfig(logging_config)

# Example usage
logger = logging.getLogger('sqlalchemy.engine')
logger.info("This is an info message from SQLAlchemy engine.")
