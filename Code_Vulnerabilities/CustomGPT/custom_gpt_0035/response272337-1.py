
import logging
import logging.config

# Example config dictionary resembling your INI format
config = {
    'version': 1,
    'loggers': {
        'sqlalchemy.engine': {
            'level': 'INFO',
            'handlers': ['console'],
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        }
    },
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    }
}

# Configure logging
logging.config.dictConfig(config)

# Example usage
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message.')
