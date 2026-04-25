
import logging
from logging.config import fileConfig

# Assuming you have a config file named 'logging.ini'
fileConfig('logging.ini')

# Now you can use the logger like this
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message')
