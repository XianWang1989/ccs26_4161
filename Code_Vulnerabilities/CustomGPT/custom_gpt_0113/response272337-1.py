
import logging
import logging.config
from configparser import ConfigParser

# Load configuration from an INI file
config = ConfigParser()
config.read('logging.ini')  # Assume your configuration is saved as logging.ini

# Set up logging
logging.config.fileConfig('logging.ini')

# Example logging usage
logger = logging.getLogger('sqlalchemy.engine')
logger.info("This is an info message.")
