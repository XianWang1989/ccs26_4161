
import logging
import logging.config
import configparser

# Assuming the config is defined in a file named 'logging.ini'
config = configparser.ConfigParser()
config.read('logging.ini')

# Setup logging configuration
logging.config.fileConfig('logging.ini')

# Example usage of the logger
logger = logging.getLogger('sqlalchemy.engine')

logger.info('This is an info message')
