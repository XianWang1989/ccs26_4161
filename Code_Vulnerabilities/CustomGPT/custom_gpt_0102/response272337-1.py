
import logging

# Create a logger
logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.INFO)

# Example of adding a console handler
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

# Example log message
logger.info('This is an information message from SQLAlchemy engine.')
