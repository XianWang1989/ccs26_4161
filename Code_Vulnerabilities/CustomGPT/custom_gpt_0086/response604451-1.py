
import ConfigParser  # Use configparser for Python 3
import telnetlib

# Read from the config file
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize the list of enabled strings
enabled_strings = []

# Check which strings are enabled based on the config
for i in range(1, 4):  # Assuming string1, string2, string3
    if config.get('Settings', f'string{i}_enable') == 'yes':
        enabled_strings.append(config.get('Settings', f'string{i}'))

# Telnet connection
tn = telnetlib.Telnet('your_telnet_server')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Match found: ", r)
