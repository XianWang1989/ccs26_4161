
import logging

# Create a logger
logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.INFO)

# Optionally add a handler if needed
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Example usage
logger.info('This is an info message')
