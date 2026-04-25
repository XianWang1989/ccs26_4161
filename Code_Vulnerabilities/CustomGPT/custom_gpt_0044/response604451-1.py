
import ConfigParser
from telnetlib import Telnet

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Get enabled strings
enabled_strings = []
for i in range(1, 4):  # Assuming you have string1, string2, string3
    string_name = f'string{i}'
    if config.get('DEFAULT', f'{string_name}_enable') == 'yes':
        enabled_strings.append(config.get('DEFAULT', string_name))

# Telnet connection example
tn = Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform the desired action
        print("Match found:", r)
