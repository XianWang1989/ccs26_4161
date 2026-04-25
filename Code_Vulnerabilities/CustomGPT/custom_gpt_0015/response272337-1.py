
import logging

# Create a logger
logger = logging.getLogger('sqlalchemy.engine')

# Set the logging level
logger.setLevel(logging.INFO)

# Create a console handler and set the level
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

# Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Example usage
logger.info('This is an info message from the SQLAlchemy engine.')
