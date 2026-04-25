
import configparser

# Create a ConfigParser instance
config = configparser.ConfigParser()

# Read the configuration file
config.read('your_config_file.ini')

# Access the values
logger_level = config.get('logger_sqlalchemy', 'level')
logger_handlers = config.get('logger_sqlalchemy', 'handlers')
logger_qualname = config.get('logger_sqlalchemy', 'qualname')

# Print to see the output
print("Logger Level:", logger_level)
print("Logger Handlers:", logger_handlers)
print("Logger Qualname:", logger_qualname)
