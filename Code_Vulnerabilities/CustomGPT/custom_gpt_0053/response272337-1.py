
import configparser

# Create a ConfigParser instance
config = configparser.ConfigParser()

# Read the configuration from a file (or string)
config.read('logging.conf')  # assuming your config is in 'logging.conf'

# Access the values
level = config['logger_sqlalchemy']['level']
handlers = config['logger_sqlalchemy']['handlers']
qualname = config['logger_sqlalchemy']['qualname']

print(f"Log Level: {level}")
print(f"Handlers: {handlers}")
print(f"Qualified Name: {qualname}")
