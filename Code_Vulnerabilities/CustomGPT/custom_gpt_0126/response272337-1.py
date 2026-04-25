
import logging
from logging.config import fileConfig

# Assuming your INI file is called 'logging.ini'
fileConfig('logging.ini')

# Create a logger
logger = logging.getLogger('sqlalchemy.engine')

# Example usage
logger.info('This is an info message')
