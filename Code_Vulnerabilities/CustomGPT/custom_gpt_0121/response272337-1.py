
import logging

# Create a logger with the specified name
logger = logging.getLogger('sqlalchemy.engine')

# Set the log level
logger.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(console_handler)

# Example log message
logger.info('This is an info message from sqlalchemy.engine.')
