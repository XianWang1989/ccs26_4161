
import configparser

# Create a config parser
config = configparser.ConfigParser()

# Read the INI file
config.read('config.ini')

# Accessing values
level = config['logger_sqlalchemy']['level']
handlers = config['logger_sqlalchemy']['handlers']
qualname = config['logger_sqlalchemy']['qualname']

print(f"Level: {level}")
print(f"Handlers: {handlers}")
print(f"Qualname: {qualname}")
