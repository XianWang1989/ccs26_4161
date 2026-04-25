
import logging
import logging.config

# Load logging configuration from an ini file
logging.config.fileConfig('logging.ini')

# Create a logger using the configured logger
logger = logging.getLogger('sqlalchemy.engine')

# Example logging
logger.info('This is an info message')
