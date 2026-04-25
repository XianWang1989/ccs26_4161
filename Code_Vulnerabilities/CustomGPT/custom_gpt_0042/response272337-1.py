
import logging
import logging.config

# Logger configuration (this would typically be in a config file)
config = {
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

# Apply the configuration
logging.config.dictConfig(config)

# Example usage
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an informational message')
