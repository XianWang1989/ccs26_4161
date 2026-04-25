
import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the configuration from a file (example.ini)
config.read('example.ini')

# Accessing the values in the section
level = config['logger_sqlalchemy']['level']
handlers = config['logger_sqlalchemy']['handlers']
qualname = config['logger_sqlalchemy']['qualname']

print(f"Level: {level}")
print(f"Handlers: {handlers}")
print(f"Qualified Name: {qualname}")
