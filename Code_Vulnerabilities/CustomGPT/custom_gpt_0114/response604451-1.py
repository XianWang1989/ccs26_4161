
import telnetlib
import ConfigParser

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Define your strings and their enabled status
strings = {
    'string1': config.get('Section', 'string1'),
    'string2': config.get('Section', 'string2'),
    'string3': config.get('Section', 'string3')
}

# List of the actual strings to search for
search_strings = [s for s, enabled in strings.items() if enabled == "yes"]

# Telnet connection setup
tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in search_strings):
        # Perform your action here
        print("Found a match!")
