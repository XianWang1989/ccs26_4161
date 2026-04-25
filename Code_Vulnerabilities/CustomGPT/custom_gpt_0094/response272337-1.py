
import logging
import logging.config
import configparser

# Load the configuration file
config = configparser.ConfigParser()
config.read('your_config.ini')

# Configure logging from the config file
logging.config.fileConfig('your_config.ini')

# Get the logger
logger = logging.getLogger('sqlalchemy.engine')

# Example log message
logger.info("This is an info log message.")
