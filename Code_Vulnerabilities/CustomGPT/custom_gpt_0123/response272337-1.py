
import logging.config
import configparser

# Read the configuration file
config = configparser.ConfigParser()
config.read('your_config_file.ini')

# Set up logging
logging.config.fileConfig('your_config_file.ini')

# Use the logger
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message.')
