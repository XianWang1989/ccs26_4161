
import logging
import logging.config
import configparser

# Load configuration from an .ini file
config = configparser.ConfigParser()
config.read('logging.ini')  # assuming your config is in 'logging.ini'

# Configure logging
logging.config.fileConfig('logging.ini')

# Use the logger
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message.')
