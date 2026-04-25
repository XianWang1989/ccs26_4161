
import logging
from logging.config import fileConfig

# Assuming a configuration file named 'logging.ini' with your syntax
fileConfig('logging.ini')

# Now you can use the configured logger
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message.')
