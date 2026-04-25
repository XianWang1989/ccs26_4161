
import logging

# Create a logger for SQLAlchemy
logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.INFO)

# You can add handlers (e.g., console, file) here if desired
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Example usage
logger.info('This is an info message from SQLAlchemy engine.')
