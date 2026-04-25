
import ConfigParser
import telnetlib

# Load the config file
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Define strings and their enabled status in the config
strings = {
    'string1': config.get('Settings', 'string1'),
    'string2': config.get('Settings', 'string2'),
    'string3': config.get('Settings', 'string3'),
}

# Create a list of enabled strings
enabled_strings = [key for key, value in strings.items() if config.get('Settings', f'{key}_enable') == 'yes']

# Telnet connection (example)
tn = telnetlib.Telnet('your.telnet.server')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Your action here
        print("Matched one of the enabled strings!")
