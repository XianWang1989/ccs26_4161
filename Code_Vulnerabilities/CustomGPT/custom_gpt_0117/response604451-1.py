
import ConfigParser
from telnetlib import Telnet

# Read the configuration file
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Grab the strings and their enabled status
strings = [
    (config.get('Settings', 'string1'), config.get('Settings', 'string1_enable')),
    (config.get('Settings', 'string2'), config.get('Settings', 'string2_enable')),
    (config.get('Settings', 'string3'), config.get('Settings', 'string3_enable')),
]

# Filter the strings based on enabled status
active_strings = [s[0] for s in strings if s[1] == 'yes']

# Example of connecting to a Telnet service
tn = Telnet('your_telnet_server', 23)

while True:
    r = tn.read_some()
    if any(x in r for x in active_strings):
        # Perform your action here
        print("Matched:", r)
