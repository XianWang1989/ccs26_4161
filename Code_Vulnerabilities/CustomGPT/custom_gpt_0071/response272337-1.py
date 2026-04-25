
import logging
import logging.config
import configparser

# Example INI content
config_data = """
[logger_sqlalchemy]
level = INFO
handlers = consoleHandler
qualname = sqlalchemy.engine

[handler_consoleHandler]
class = StreamHandler
level = INFO
formatter = simpleFormatter
args = []

[formatter_simpleFormatter]
format = %(asctime)s - %(name)s - %(levelname)s - %(message)s
"""

# Load the configuration
config = configparser.ConfigParser()
config.read_string(config_data)

# Configure logging
logging.config.fileConfig(config)

# Use the logger
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message.')
