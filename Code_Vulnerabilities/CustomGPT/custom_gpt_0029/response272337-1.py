
import configparser

# Create a ConfigParser instance
config = configparser.ConfigParser()

# Read the configuration from a file or string
config.read_string("""
[logger_sqlalchemy]
level = INFO
handlers =
qualname = sqlalchemy.engine
""")

# Access the values
level = config['logger_sqlalchemy']['level']
handlers = config['logger_sqlalchemy']['handlers']
qualname = config['logger_sqlalchemy']['qualname']

print(f"Level: {level}")
print(f"Handlers: {handlers}")
print(f"Qualname: {qualname}")
