
import ConfigParser
from telnetlib import Telnet

# Load the configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize your list of strings and their enabled settings
strings = [
    ("string1", config.get('DEFAULT', 'string1_enable', fallback='no')),
    ("string2", config.get('DEFAULT', 'string2_enable', fallback='no')),
    ("string3", config.get('DEFAULT', 'string3_enable', fallback='no'))
]

# Prepare the active strings based on enabled settings
active_strings = [s for s, enabled in strings if enabled.lower() == 'yes']

# Assuming you have already established a telnet connection
tn = Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in active_strings):
        # Perform your action
        print("Match found!")
