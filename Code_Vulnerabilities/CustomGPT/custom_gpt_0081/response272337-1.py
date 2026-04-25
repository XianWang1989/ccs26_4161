
import logging
import logging.config
import sqlalchemy

# Example configuration dict equivalent to your INI file
logging_config = {
    'version': 1,
    'loggers': {
        'sqlalchemy.engine': {
            'level': 'INFO',
            'handlers': [],
        },
    }
}

# Configure logging using the above dictionary
logging.config.dictConfig(logging_config)

# Create a logger instance for sqlalchemy.engine
logger = logging.getLogger('sqlalchemy.engine')

# Example usage of the logger
logger.info('This message will be logged if the level is INFO or lower.')

# Typical usage in a SQLAlchemy context:
engine = sqlalchemy.create_engine('sqlite:///:memory:')
# Now, when you perform operations with this engine, SQLAlchemy will log accordingly.
