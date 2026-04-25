
import logging
import logging.config
import configparser

# Load the configuration from the config file
config = configparser.ConfigParser()
config.read('logging.ini')  # Assuming your config file is named logging.ini

# Configure logging based on the configuration
logging.config.fileConfig('logging.ini')

# Get the logger
logger = logging.getLogger('sqlalchemy.engine')

# Example log statements
logger.info("This is an info message.")
logger.warning("This is a warning message.")
