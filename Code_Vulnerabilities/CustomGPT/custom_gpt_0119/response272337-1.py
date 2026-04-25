
import logging
import logging.config
import configparser

# Assuming config.ini is your config file containing the provided syntax
config = configparser.ConfigParser()
config.read('config.ini')

# Setup logging configuration from the config file
logging.config.fileConfig('config.ini')

# Now you can use the logger
logger = logging.getLogger('sqlalchemy.engine')

logger.info('This is an info message.')
