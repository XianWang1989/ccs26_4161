
import logging

# Create a logger
logger = logging.getLogger('sqlalchemy.engine')

# Set the level of the logger
logger.setLevel(logging.INFO)

# Create a console handler
handler = logging.StreamHandler()

# Setting the logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Example usage
logger.info("This is an information message.")
