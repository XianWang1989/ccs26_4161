
import logging
import logging.config

# Sample logging configuration dictionary
logging_config = {
    'loggers': {
        'sqlalchemy.engine': {
            'level': 'INFO',
            'handlers': ['console'],  # Assuming you defined a console handler.
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'simple',
        }
    },
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(levelname)s - %(message)s',
        }
    }
}

if __name__ == "__main__":
    logging.config.dictConfig(logging_config)
    logger = logging.getLogger('sqlalchemy.engine')
    logger.info('This is an info message.')
