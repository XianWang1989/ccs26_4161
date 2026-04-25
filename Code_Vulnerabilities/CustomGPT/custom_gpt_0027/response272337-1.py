
import logging

# Create a custom logger for SQLAlchemy
logger = logging.getLogger('sqlalchemy.engine')

# Set the logging level
logger.setLevel(logging.INFO)

# Create a console handler
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Example log message
logger.info("This is an info message from SQLAlchemy.")
