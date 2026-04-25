
import logging
import logging.config
import configparser

# Sample INI configuration content
config_content = """
[logger_sqlalchemy]
level = INFO
handlers =
qualname = sqlalchemy.engine
"""

# Write the configuration to a temporary file
with open('logging_config.ini', 'w') as config_file:
    config_file.write(config_content)

# Load the configuration
config = configparser.ConfigParser()
config.read('logging_config.ini')

# Set up logging
logging.config.fileConfig('logging_config.ini', disable_existing_loggers=False)

# Example usage of logger
logger = logging.getLogger('sqlalchemy.engine')
logger.info("This is an info message")
