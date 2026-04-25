
import logging
import logging.config
import configparser

# Sample INI configuration as a string
config_str = """
[logger_sqlalchemy]
level = INFO
handlers = consoleHandler
qualname = sqlalchemy.engine

[handler_consoleHandler]
class = StreamHandler
level = INFO
formatter = simpleFormatter
args =

[formatter_simpleFormatter]
format = %(asctime)s - %(name)s - %(levelname)s - %(message)s
"""

# Write the config to file (in practice, this would be a file)
with open('logging_config.ini', 'w') as f:
    f.write(config_str)

# Read the configuration
config = configparser.ConfigParser()
config.read('logging_config.ini')

# Configure logging
logging.config.fileConfig('logging_config.ini')

# Create a logger
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message.')
