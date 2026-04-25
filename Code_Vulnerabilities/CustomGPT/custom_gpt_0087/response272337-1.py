
import logging
import logging.config

# Assuming you load your configuration from a file named 'logging.ini'
logging.config.fileConfig('logging.ini')

# Now you can use the logger
logger = logging.getLogger('sqlalchemy.engine')

# Log an example message
logger.info('This is an info message from SQLAlchemy.')
