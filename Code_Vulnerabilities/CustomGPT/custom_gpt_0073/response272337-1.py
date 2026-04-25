
import logging
from logging.config import fileConfig

# Assuming you have a configuration file (e.g., logging.ini)
fileConfig('logging.ini')

# Create a logger
logger = logging.getLogger('sqlalchemy.engine')

# Example usage of the logger
logger.info('This is an INFO message from SQLAlchemy.')
