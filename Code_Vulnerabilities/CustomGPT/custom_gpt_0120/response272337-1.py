
import logging
import logging.config
import configparser

# Assuming you have a configuration file named logging.ini
config = configparser.ConfigParser()
config.read('logging.ini')

# Configure logging based on the configuration file
logging.config.fileConfig('logging.ini')

logger = logging.getLogger('sqlalchemy.engine')

# Example logging
logger.info('This is an info message related to SQLAlchemy')
