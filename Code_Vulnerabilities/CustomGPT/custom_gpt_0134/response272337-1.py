
import logging
import logging.config
import configparser

# Example INI-style configuration
config = """
[logger_sqlalchemy]
level = INFO
handlers = 
qualname = sqlalchemy.engine
"""

# Reading the configuration
config_parser = configparser.ConfigParser()
config_parser.read_string(config)

# Configure logging
logging.config.fileConfig(config_parser)

# Example usage
logger = logging.getLogger('sqlalchemy.engine')
logger.info("This is an info message for SQLAlchemy.")
