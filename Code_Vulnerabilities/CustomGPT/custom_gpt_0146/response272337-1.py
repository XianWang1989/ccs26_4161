
import logging
import logging.config
import configparser

# Create a config parser to read the configuration file
config = configparser.ConfigParser()
config.read('your_config.ini')  # Assume your config is saved as 'your_config.ini'

# Setup logging using the configuration
logging.config.fileConfig('your_config.ini')

# Now you can use the logger
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message.')
