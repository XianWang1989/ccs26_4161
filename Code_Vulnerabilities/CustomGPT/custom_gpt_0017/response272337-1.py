
import logging
import logging.config
import configparser

# Load the configuration from the INI-style file
config = configparser.ConfigParser()
config.read('logging.ini')  # Assume the above configuration is in logging.ini

# Configure logging
logging.config.fileConfig('logging.ini')

# Create a logger
logger = logging.getLogger('sqlalchemy.engine')

# Log a message
logger.info("This is an info message.")
