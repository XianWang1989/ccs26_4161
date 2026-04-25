
import logging
from sqlalchemy import create_engine

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('sqlalchemy.engine')

# Example SQLAlchemy usage
engine = create_engine('sqlite:///:memory:')
logger.info("SQLAlchemy engine created.")
