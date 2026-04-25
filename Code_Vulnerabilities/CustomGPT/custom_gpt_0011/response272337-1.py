
import logging

# Example of configuring a logger programmatically
logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.INFO)

# Create a console handler for the logger
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and set it for the console handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(console_handler)

# Example log message
logger.info('This is an info message from the sqlalchemy.engine logger.')
