
import logging
import logging.config
import configparser

# Read the configuration
config = configparser.ConfigParser()
config.read('logging.ini')

# Setup logging
logging.config.fileConfig('logging.ini')

# Example usage of the logger
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message.')
