
import logging

# Configure logging for SQLAlchemy
logging.basicConfig(level=logging.INFO)

# Create a logger
logger = logging.getLogger('sqlalchemy.engine')

# Example logging
logger.info('This is an info message from SQLAlchemy.')
