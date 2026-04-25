
import logging
from logging.config import fileConfig

# Assuming a logging configuration file like the one described
fileConfig('logging.conf')

# Creating a logger
logger = logging.getLogger('sqlalchemy.engine')

# Logging an example message
logger.info('This is an info message.')
