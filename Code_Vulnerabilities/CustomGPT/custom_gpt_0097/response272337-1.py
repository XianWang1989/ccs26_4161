
import logging
import logging.config
import configparser

# Read configuration from a file
config = configparser.ConfigParser()
config.read('logging.ini')  # Your config file

# Configure logging
logging.config.fileConfig('logging.ini')

# Using the logger
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message.')
