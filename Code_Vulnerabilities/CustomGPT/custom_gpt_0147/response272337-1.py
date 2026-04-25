
import logging
import logging.config
from configparser import ConfigParser

# Example config string to simulate an ini file
config_string = """
[logger_sqlalchemy]
level = INFO
handlers = console
qualname = sqlalchemy.engine

[handler_console]
class = StreamHandler
level = INFO
formatter = simple
args = []

[formatter_simple]
format = %(asctime)s - %(name)s - %(levelname)s - %(message)s
"""

# Creating a ConfigParser object and reading the config string
config = ConfigParser()
config.read_string(config_string)

# Setting up logging configuration from the config
logging.config.fileConfig(config)

# Example usage of the logger
logger = logging.getLogger('sqlalchemy.engine')
logger.info("This is an info message from SQLAlchemy logger.")
logger.error("This is an error message from SQLAlchemy logger.")
