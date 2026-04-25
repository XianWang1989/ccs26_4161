import logging
import logging.config

logging.config.fileConfig('development.ini')  # loads settings from your .ini file
logger = logging.getLogger('sqlalchemy.engine')
logger.info("This is a test log.")
