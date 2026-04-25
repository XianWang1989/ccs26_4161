
import configparser

# Create a ConfigParser instance
config = configparser.ConfigParser()

# Read the configuration file
config.read('my_config.ini')

# Access the logger settings
log_level = config['logger_sqlalchemy']['level']
log_handlers = config['logger_sqlalchemy']['handlers']
log_qualname = config['logger_sqlalchemy']['qualname']

print(f"Level: {log_level}, Handlers: {log_handlers}, Qualname: {log_qualname}")
