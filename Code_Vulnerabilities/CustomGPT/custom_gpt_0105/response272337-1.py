
import logging
import logging.config

# Assuming this config is read from a file named 'logging.ini'
logging.config.fileConfig('logging.ini')

# Example logger usage
logger = logging.getLogger('sqlalchemy.engine')
logger.info("This is an info message.")
