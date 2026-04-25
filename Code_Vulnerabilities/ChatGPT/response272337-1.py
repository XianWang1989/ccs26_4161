
import logging
import logging.config
import configparser

# Assuming the config is in a file 'logging.ini'
config = configparser.ConfigParser()
config.read('logging.ini')

# Set up logging using the configuration file
logging.config.fileConfig('logging.ini')

# Get the logger
logger = logging.getLogger('sqlalchemy')

# Now you can use the logger
logger.info('This is an info message.')
