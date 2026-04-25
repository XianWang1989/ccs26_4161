
import ConfigParser
from telnetlib import Telnet

# Read config
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Retrieve strings and their enabled status
strings = [
    ('string1', config.get('SECTION', 'string1_enable'), 'string1_value'),
    ('string2', config.get('SECTION', 'string2_enable'), 'string2_value'),
    ('string3', config.get('SECTION', 'string3_enable'), 'string3_value'),
]

# Build a list of enabled strings
enabled_strings = [value for name, enabled, value in strings if enabled.lower() == 'yes']

# Connect to Telnet
tn = Telnet('hostname', port)

# Reading and searching
while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Match found! Performing action...")

