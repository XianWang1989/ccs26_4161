
import configparser

# Create a config parser
config = configparser.ConfigParser()

# Example of reading an INI file
config.read('your_config.ini')

# Accessing the logger configuration
logger_level = config['logger_sqlalchemy']['level']
logger_handlers = config['logger_sqlalchemy']['handlers']
logger_qualname = config['logger_sqlalchemy']['qualname']

print(f"Logger Level: {logger_level}")
print(f"Logger Handlers: {logger_handlers}")
print(f"Logger Qualname: {logger_qualname}")
