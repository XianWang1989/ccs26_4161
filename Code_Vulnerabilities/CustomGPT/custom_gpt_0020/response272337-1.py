
import logging

# Configure logging to also handle SQLAlchemy logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('sqlalchemy.engine')

# Now we can log an INFO level message
logger.info("This is an info message from the SQLAlchemy engine.")
