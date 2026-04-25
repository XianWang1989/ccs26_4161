
import logging.config
import configparser

# Create a config parser
config = configparser.ConfigParser()
config.read('logging.ini')  # Assume your config is in logging.ini

# Set up logging from the configuration
logging.config.fileConfig('logging.ini')

# Example usage of the logger
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message.')
