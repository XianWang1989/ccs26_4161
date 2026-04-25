
import logging
from logging.config import fileConfig

# Assuming you have a logging configuration file 'logging.ini'
fileConfig('logging.ini')

# Create a logger
logger = logging.getLogger('sqlalchemy.engine')

# Log a message
logger.info("This is an info message from SQLAlchemy.")
