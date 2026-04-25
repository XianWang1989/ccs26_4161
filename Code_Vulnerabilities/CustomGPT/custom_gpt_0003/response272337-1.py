
import logging

# Create a logger
logger = logging.getLogger('sqlalchemy.engine')

# Set the level of the logger
logger.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()

# Create a formatter and attach it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(console_handler)

# Example usage of the logger
logger.info('This is an info message related to SQLAlchemy engine.')
