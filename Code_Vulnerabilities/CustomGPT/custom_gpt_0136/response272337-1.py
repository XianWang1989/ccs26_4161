
import configparser

# Create a config parser
config = configparser.ConfigParser()

# Read the configuration file
config.read('your_config.ini')

# Accessing values
level = config['logger_sqlalchemy']['level']
handlers = config['logger_sqlalchemy']['handlers']
qualname = config['logger_sqlalchemy']['qualname']

print(f"Level: {level}")
print(f"Handlers: {handlers}")
print(f"Qualname: {qualname}")
