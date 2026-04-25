
import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the INI file
config.read('your_config.ini')

# Accessing the logger_sqlalchemy section
sqlalchemy_logger = config['logger_sqlalchemy']

# Retrieve settings
level = sqlalchemy_logger.get('level')
handlers = sqlalchemy_logger.get('handlers', '')
qualname = sqlalchemy_logger.get('qualname')

print(f'Level: {level}, Handlers: {handlers}, Qualname: {qualname}')
