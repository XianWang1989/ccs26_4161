
import logging
import logging.config
import configparser

# Load the configuration file
config = configparser.ConfigParser()
config.read('logging.ini')  # assuming your INI file is named logging.ini

# Configure logging
logging.config.fileConfig('logging.ini')

# Example usage
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message.')
