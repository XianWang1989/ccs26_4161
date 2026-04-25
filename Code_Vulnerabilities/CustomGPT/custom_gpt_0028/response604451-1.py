
import ConfigParser
from telnetlib import Telnet

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize Telnet connection
tn = Telnet('your_telnet_host')

# Define strings and their enabled status
search_strings = [
    ('string1', config.get('Settings', 'string1_enable')),
    ('string2', config.get('Settings', 'string2_enable')),
    ('string3', config.get('Settings', 'string3_enable')),
]

# Filter enabled search strings
enabled_strings = [s for s, enabled in search_strings if enabled == 'yes']

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Match found!")
