
import logging
import logging.config
import configparser

# Read the configuration file
config = configparser.ConfigParser()
config.read('your_config_file.ini')

# Set up logging
logging.config.fileConfig('your_config_file.ini')

# Using the logger
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message about SQLAlchemy.')
