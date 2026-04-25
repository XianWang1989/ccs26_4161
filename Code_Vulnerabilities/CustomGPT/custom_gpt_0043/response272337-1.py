
import logging
import logging.config
import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()
config.read('logging.ini')  # Assume your config is stored in this file

# Configure logging from the configuration file
logging.config.fileConfig('logging.ini')

# Example usage of logging
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message from SQLAlchemy log.')
