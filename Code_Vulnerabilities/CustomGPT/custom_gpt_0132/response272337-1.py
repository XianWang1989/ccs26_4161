
import logging
from logging.config import fileConfig

# Load the logging configuration from a .ini file
fileConfig('logging_config.ini')

# Create a logger
logger = logging.getLogger('sqlalchemy.engine')

# Example usage of logger
logger.info('This is an info message')
