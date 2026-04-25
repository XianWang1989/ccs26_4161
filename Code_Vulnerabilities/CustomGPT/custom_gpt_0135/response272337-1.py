
import logging

# Configuration for the logger
logging.basicConfig(level=logging.INFO)

# Create a specific logger for sqlalchemy.engine
sqlalchemy_logger = logging.getLogger('sqlalchemy.engine')

# Example of logging at different levels
sqlalchemy_logger.debug("This is a debug message, not shown due to level.")
sqlalchemy_logger.info("This is an info message, it will be shown.")
sqlalchemy_logger.warning("This is a warning, it will also be shown.")
