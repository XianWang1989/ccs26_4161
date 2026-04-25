
import logging.config
import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()
config.read('your_config.ini')  # Replace with your actual config file

# Configure logging
logging.config.fileConfig('your_config.ini')

# Example usage of the logger
logger = logging.getLogger('sqlalchemy.engine')

logger.info('This is a log message.')
