
import ConfigParser
from telnetlib import Telnet

# Load the configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize your telnet connection (replace with actual details)
tn = Telnet('your.telnet.server')

# Prepare your search strings
strings = ['string1', 'string2', 'string3']
enabled_strings = []

# Check which strings are enabled in the config
for s in strings:
    if config.get('Settings', f'{s}_enable') == 'yes':
        enabled_strings.append(s)

# Read from telnet and check for enabled strings
while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action
        print("Found one of the enabled strings!")
