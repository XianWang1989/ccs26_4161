
import logging
import logging.config
import yaml  # You might use a library like pyyaml to read it

# Example of logging configuration similar to your INI format
logging_config = """
loggers:
  sqlalchemy:
    level: INFO
    handlers: []
    qualname: sqlalchemy.engine
"""

# Load logging configuration
logging.config.dictConfig(yaml.safe_load(logging_config))

# Example logger
logger = logging.getLogger('sqlalchemy.engine')

# Log a message
logger.info("This is an info message.")
