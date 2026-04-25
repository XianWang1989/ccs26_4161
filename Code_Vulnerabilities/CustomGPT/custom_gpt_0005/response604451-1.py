
import ConfigParser
from telnetlib import Telnet

# Load the configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Establish Telnet connection
tn = Telnet('your_telnet_host')

# Retrieve enabled strings dynamically
enabled_strings = []
for i in range(1, 4):  # Assuming you have string1, string2, string3
    string_name = f'string{i}'
    if config.get('DEFAULT', f'{string_name}_enable') == 'yes':
        enabled_strings.append(config.get('DEFAULT', string_name))

# Continuous reading loop
while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform action
        print("Match found!")
