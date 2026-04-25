
import logging
import logging.config
import configparser

# Read the configuration from a file
config = configparser.ConfigParser()
config.read('logging.conf')  # Assume your configuration is in this file

# Configure the logging
logging.config.fileConfig('logging.conf')

# Example usage of the logger
logger = logging.getLogger('sqlalchemy.engine')

# Log a message
logger.info('This is an info message.')
