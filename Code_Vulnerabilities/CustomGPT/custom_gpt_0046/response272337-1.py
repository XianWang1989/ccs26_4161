
import logging

# Creating a logger for SQLAlchemy
logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.INFO)

# Example of logging
logger.info('This is an info message from SQLAlchemy')
