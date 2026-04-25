
import configparser

# Create a config parser instance
config = configparser.ConfigParser()

# Read the INI file
config.read('your_config_file.ini')

# Access the logger_sqlalchemy settings
level = config['logger_sqlalchemy']['level']
handlers = config['logger_sqlalchemy']['handlers']
qualname = config['logger_sqlalchemy']['qualname']

print(f"Log Level: {level}")
print(f"Handlers: {handlers}")
print(f"Qualified Name: {qualname}")
