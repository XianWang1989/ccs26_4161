
import logging

# Create a logger
logger = logging.getLogger('sqlalchemy.engine')

# Set the logging level
logger.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

# Example usage of the logger
logger.info('This is an info message for SQLAlchemy engine.')
