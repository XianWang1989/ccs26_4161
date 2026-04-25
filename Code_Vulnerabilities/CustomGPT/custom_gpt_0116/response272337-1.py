
import logging
import logging.config
import configparser

# Parse the configuration file
config = configparser.ConfigParser()
config.read('logging.ini')  # Assume your INI file is named logging.ini

# Configure logging
logging.config.fileConfig('logging.ini')

# Use the logger
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message')
