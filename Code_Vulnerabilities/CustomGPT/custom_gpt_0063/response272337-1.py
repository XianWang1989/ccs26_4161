
import logging
import logging.config

# Example configuration as a dictionary.
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

logging.config.dictConfig(logging_config)
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message from SQLAlchemy')
