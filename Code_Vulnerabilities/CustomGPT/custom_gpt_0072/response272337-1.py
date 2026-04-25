
import logging
from logging.config import fileConfig

# Load the configuration
fileConfig('path/to/your/config.ini')

# Now you can use the logger
logger = logging.getLogger('sqlalchemy.engine')

# Example log message
logger.info('This is an info message')
