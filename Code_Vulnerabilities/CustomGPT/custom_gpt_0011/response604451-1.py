
import ConfigParser
from telnetlib import Telnet

# Initialize ConfigParser and read your configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Retrieve the strings and their enabled status
string1 = 'your_string1'
string2 = 'your_string2'
string3 = 'your_string3'

# Collect enabled strings based on the config
enabled_strings = []
if config.get('DEFAULT', 'string1_enable') == 'yes':
    enabled_strings.append(string1)
if config.get('DEFAULT', 'string2_enable') == 'yes':
    enabled_strings.append(string2)
if config.get('DEFAULT', 'string3_enable') == 'yes':
    enabled_strings.append(string3)

# Example Telnet connection
tn = Telnet('your_telnet_server')
while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Action performed based on matched string!")
