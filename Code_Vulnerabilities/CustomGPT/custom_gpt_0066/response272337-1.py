
import logging
import logging.config

# Example of how to configure logging using a dictionary (similar to your INI example)
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

# Example logger usage
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message.')
