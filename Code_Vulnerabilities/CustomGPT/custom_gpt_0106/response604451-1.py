
import ConfigParser
import telnetlib

# Load your configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize your strings and their enable states
strings = {
    'string1': config.get('DEFAULT', 'string1_enable'),
    'string2': config.get('DEFAULT', 'string2_enable'),
    'string3': config.get('DEFAULT', 'string3_enable')
}

# Create a list of active search strings
active_strings = [key for key, value in strings.items() if value == 'yes']

# Connect to telnet
tn = telnetlib.Telnet('your.telnet.server')

while True:
    r = tn.read_some()
    if any(x in r for x in active_strings):
        # Perform your action here
        print("Found a match!")
