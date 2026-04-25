
import logging
from pyramid.config import Configurator

# Set up logging
config = Configurator()
config.add_settings({
    'logger_sqlalchemy.level': 'INFO',
    'logger_sqlalchemy.handlers': '',  # Define your handlers here
    'logger_sqlalchemy.qualname': 'sqlalchemy.engine'
})

# Configure logging
logging.config.fileConfig('your_logging_config.ini')

# Example usage
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message.')
