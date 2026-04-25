
import logging
from logging.config import fileConfig

# Load the logging configuration
fileConfig('logging.ini')  # Assuming your config is in logging.ini

# Use the logger
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message')
