
import logging
from sqlalchemy import create_engine

# Set up logging for SQLAlchemy
logging.basicConfig()
logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.INFO)

# Example of creating an engine, which would invoke logging
engine = create_engine('sqlite:///:memory:', echo=True)

# The engine operations here would generate logs at the INFO level
