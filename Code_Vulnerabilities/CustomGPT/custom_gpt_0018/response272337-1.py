
import configparser

# Assuming config.ini contains your INI configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Accessing the logging settings
log_level = config['logger_sqlalchemy']['level']
log_qualname = config['logger_sqlalchemy']['qualname']

print(log_level)  # Outputs: INFO
print(log_qualname)  # Outputs: sqlalchemy.engine
