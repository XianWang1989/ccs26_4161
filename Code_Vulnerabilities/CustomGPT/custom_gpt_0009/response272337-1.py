
import logging
import logging.config
import configparser

# Create a simple config.ini to mimic the example setup
config = configparser.ConfigParser()
config['logger_sqlalchemy'] = {
    'level': 'INFO',
    'handlers': 'console',
    'qualname': 'sqlalchemy.engine'
}
config['handler_console'] = {
    'class': 'logging.StreamHandler',
    'level': 'INFO',
}

# Applying the config
logging.config.fileConfig(config)

# Create logger
logger = logging.getLogger('sqlalchemy.engine')

# Example log message
logger.info('This is an info message from SQLAlchemy logger.')
