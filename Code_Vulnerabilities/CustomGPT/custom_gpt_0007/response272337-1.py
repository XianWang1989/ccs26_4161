
import logging
from logging.config import fileConfig

# Suppose you have a logging configuration file 'logging.ini'
fileConfig('logging.ini')

# Now you can use the logger
logger = logging.getLogger('sqlalchemy.engine')
logger.info("This is an info message from SQLAlchemy engine.")
