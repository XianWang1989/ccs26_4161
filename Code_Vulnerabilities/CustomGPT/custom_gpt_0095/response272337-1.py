
import logging
import logging.config
import sqlalchemy

# Load logging configuration (this can be from an INI file)
logging.config.fileConfig('logging.ini')

# Create a logger
logger = logging.getLogger('sqlalchemy.engine')

# Use the logger
logger.info('This is an info message.')

# Example of connecting to a database with SQLAlchemy
engine = sqlalchemy.create_engine('sqlite:///:memory:')
