
logger_config = {
    'level': 'INFO',
    'handlers': [],
    'qualname': 'sqlalchemy.engine'
}

# Example usage of the logger config
import logging
import logging.config

logging.config.dictConfig({
    'version': 1,
    'loggers': {
        'sqlalchemy.engine': {
            'level': logger_config['level'],
            'handlers': logger_config['handlers'],
        },
    },
})

logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message.')
