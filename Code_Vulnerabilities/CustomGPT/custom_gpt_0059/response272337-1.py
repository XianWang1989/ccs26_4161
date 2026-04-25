
import logging

# Create a logger for sqlalchemy
logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.INFO)

# Here you could add handlers if needed
handler = logging.StreamHandler()  # Example handler
logger.addHandler(handler)

logger.info('This is an info message')
