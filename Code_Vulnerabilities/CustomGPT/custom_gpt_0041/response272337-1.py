
import logging
import logging.config
import configparser

# Read the configuration file
config = configparser.ConfigParser()
config.read('logging.ini')

# Configure logging
logging.config.fileConfig('logging.ini')

# Example of using the logger
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message.')
