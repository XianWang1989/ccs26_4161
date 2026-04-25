
import logging
import logging.config
import configparser

# Load configuration from an .ini file
config = configparser.ConfigParser()
config.read('logging.ini')

# Configure logging based on the config file
logging.config.fileConfig('logging.ini')

# Example usage
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an informational message.')
