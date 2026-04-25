
import logging
import logging.config

# Assuming your INI file is named 'logging.ini'
logging.config.fileConfig('logging.ini')

# Now you can use the logger
logger = logging.getLogger('sqlalchemy.engine')

# Example log message
logger.info('This is an info message from SQLAlchemy.')
