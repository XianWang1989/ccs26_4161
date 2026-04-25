
import configparser
import logging

# Create a configuration parser
config = configparser.ConfigParser()
config.read('logging.ini')  # assuming your logging settings are in 'logging.ini'

# Configure logging based on the config
logging.basicConfig(level=config['logger_sqlalchemy'].get('level', 'WARNING'))
logger = logging.getLogger(config['logger_sqlalchemy']['qualname'])
logger.info("This is an info message")
