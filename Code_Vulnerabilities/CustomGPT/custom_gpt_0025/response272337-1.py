
import logging
import logging.config
import configparser

# Simulate reading from a configuration file
config_string = """
[logger_sqlalchemy]
level = INFO
handlers =
qualname = sqlalchemy.engine
"""

# Writing to a temporary config file
with open('logging.ini', 'w') as config_file:
    config_file.write(config_string)

# Set up logging from the configuration
config = configparser.ConfigParser()
config.read('logging.ini')

logging.config.fileConfig('logging.ini')

# Example logger usage
logger = logging.getLogger('sqlalchemy.engine')
logger.info("This is an info message.")
logger.debug("This debug message won't be shown due to the INFO level.")
