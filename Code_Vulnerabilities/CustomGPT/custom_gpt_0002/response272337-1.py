
import logging
import logging.config
from configparser import ConfigParser

# Load configuration from INI file
config = ConfigParser()
config.read('logging.ini')

# Configure logging
logging.config.fileConfig('logging.ini')

# Example usage of the logger
logger = logging.getLogger('sqlalchemy.engine')
logger.info("This is an info log from sqlalchemy.")
