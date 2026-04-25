
import logging

# Configuring logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('sqlalchemy.engine')

# Example usage
logger.info('This is an info message.')
