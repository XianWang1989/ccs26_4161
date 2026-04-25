
import logging.config
import configparser

# Create a ConfigParser instance
config = configparser.ConfigParser()
config.read('logging.ini')  # Read the INI file

# Configure logging
logging.config.fileConfig('logging.ini', disable_existing_loggers=False)

# Example of using the logger
logger = logging.getLogger('sqlalchemy.engine')

logger.info('This is an info message')
