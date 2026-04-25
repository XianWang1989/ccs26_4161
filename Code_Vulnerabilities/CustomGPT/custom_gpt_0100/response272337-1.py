
import logging
import logging.config
import configparser

# Load the configuration
config = configparser.ConfigParser()
config.read('logging.ini')  # Assuming your config is saved in logging.ini

# Set up the logging configuration
logging.config.fileConfig('logging.ini')

# Now you can use the logger
logger = logging.getLogger('sqlalchemy.engine')
logger.info("This is an info message from SQLAlchemy.")
