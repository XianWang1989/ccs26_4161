
import logging
from logging.config import fileConfig

# Assume you have a logging.ini file with the above content
fileConfig('logging.ini')

# Now, you can get a logger
logger = logging.getLogger('sqlalchemy.engine')

logger.info("This is an info message.")
