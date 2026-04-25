
import logging

# Configure the SQLAlchemy logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('sqlalchemy.engine')

# Example logging
logger.info("This is an informative message from SQLAlchemy engine.")
