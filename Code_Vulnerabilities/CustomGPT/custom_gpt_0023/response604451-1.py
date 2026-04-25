
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Function to get enabled strings from config
def get_enabled_strings(config):
    strings = []
    for key in config.options('Strings'):
        if config.getboolean('Strings', key):  # Cast to boolean
            strings.append(key)  # Append to the list of enabled strings
    return strings

# Connect to Telnet
tn = telnetlib.Telnet('your_telnet_host')

# List of strings to search (assuming string names match the keys in the config)
enabled_strings = get_enabled_strings(config)

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Your action here
        print("Found one of the enabled strings!")
