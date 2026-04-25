
import logging
from logging.config import fileConfig

# Load the logging configuration from an ini file
fileConfig('logging.ini')  # Assume your settings are saved in logging.ini

# Get the logger
logger = logging.getLogger('sqlalchemy.engine')

# Now you can use the logger
logger.info('This is an info message.')
