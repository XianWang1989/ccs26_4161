
import logging
import logging.config
import configparser

# Example: Reading from a config file
config = configparser.ConfigParser()
config.read('logging.ini')  # Your config file name

# Configure logging using the config
logging.config.fileConfig('logging.ini')

# Get the SQLAlchemy logger
logger = logging.getLogger('sqlalchemy.engine')

# Example usage of logger
logger.info("This is an information message.")
