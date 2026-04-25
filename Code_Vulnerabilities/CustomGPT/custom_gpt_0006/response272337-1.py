
import logging
import logging.config
import configparser

# Sample configuration string
config_string = """
[logger_sqlalchemy]
level = INFO
handlers =
qualname = sqlalchemy.engine
"""

# Create a config parser
config = configparser.ConfigParser()
config.read_string(config_string)

# Set up logging
logging.config.fileConfig(config)

# Example usage of logging
logger = logging.getLogger('sqlalchemy.engine')
logger.info('This is an info message.')
