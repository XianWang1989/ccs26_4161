
import logging
import logging.config
from configparser import ConfigParser

# Load configuration
config = ConfigParser()
config.read('path/to/config.ini')

# Set up logging
logging.config.fileConfig('path/to/config.ini')

# Example logger usage
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message.')
