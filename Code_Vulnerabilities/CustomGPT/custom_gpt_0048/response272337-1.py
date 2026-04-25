
import logging.config
import configparser

# Create a sample logger configuration
config_str = """
[logger_sqlalchemy]
level = INFO
handlers = console
qualname = sqlalchemy.engine

[handler_console]
class = StreamHandler
level = DEBUG
args =
"""

# Parse the configuration
config = configparser.ConfigParser()
config.read_string(config_str)

# Setup logging
logging.config.fileConfig(config)

# Example logger usage
logger = logging.getLogger('sqlalchemy.engine')
logger.info("This is an info message.")
