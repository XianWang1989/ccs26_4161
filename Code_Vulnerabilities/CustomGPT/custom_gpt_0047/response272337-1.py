
import logging

# Create a custom logger
logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.INFO)

# Create handlers (e.g., console handler)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

# Create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Example usage
logger.info('This is an informational message for SQLAlchemy engine.') 
