
import logging
import logging.config

# Assuming you have the above configuration in a file named 'logging.conf'.

# Load config from the file
logging.config.fileConfig('logging.conf')

# Create a logger
logger = logging.getLogger('sqlalchemy.engine')

# Now you can use this logger
logger.info('This is an info message for SQLAlchemy!')
