
import logging

# Create a logger for SQLAlchemy
logger = logging.getLogger('sqlalchemy.engine')

# Set the logging level
logger.setLevel(logging.INFO)

# Create a handler (here using console for simplicity)
handler = logging.StreamHandler()

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Example logging
logger.info('This is an info message')
