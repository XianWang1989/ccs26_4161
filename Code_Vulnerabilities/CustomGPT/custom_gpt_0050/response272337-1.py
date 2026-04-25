
import logging

# Create a logger
logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.INFO)

# You can add handlers here if needed
# For example, adding a console handler
handler = logging.StreamHandler()
logger.addHandler(handler)

# Example log message
logger.info('This is an info message.')
