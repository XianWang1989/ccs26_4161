
import configparser

# Create a config parser
config = configparser.ConfigParser()

# Read the configuration from a file (e.g., `config.ini`)
config.read('config.ini')

# Accessing the values
level = config['logger_sqlalchemy']['level']
handlers = config['logger_sqlalchemy']['handlers']
qualname = config['logger_sqlalchemy']['qualname']

print(f"Level: {level}, Handlers: {handlers}, Qualname: {qualname}")
