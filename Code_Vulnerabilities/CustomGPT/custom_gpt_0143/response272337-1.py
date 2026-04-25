
import configparser
import logging

# Create a config parser
config = configparser.ConfigParser()
config.read('config.ini')  # Assuming your config is saved in config.ini

# Set up logging based on the configuration
log_level = config['logger_sqlalchemy']['level']
logging.basicConfig(level=log_level)
logger = logging.getLogger(config['logger_sqlalchemy']['qualname'])

# Example usage
logger.info('This is an info message.')
