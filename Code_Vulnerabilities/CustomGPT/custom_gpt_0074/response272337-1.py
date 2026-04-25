
import logging

# Create a logger
logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.INFO)

# Create console handler (you can define other handlers as needed)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

# Now you can log messages
logger.info("This is an info message!")
