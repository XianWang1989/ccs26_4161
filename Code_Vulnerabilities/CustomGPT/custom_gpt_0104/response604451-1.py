
import ConfigParser
from telnetlib import Telnet

# Read from the config.ini file
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize the Telnet connection (replace with your actual host and port)
tn = Telnet('your_telnet_host', your_port_number)

# List of strings to check against
strings_to_check = ['string1', 'string2', 'string3']
enabled_strings = []

# Collect enabled strings based on config settings
for string in strings_to_check:
    if config.get('Default', f'{string}_enable') == 'yes':
        enabled_strings.append(string)

# Now use enabled_strings in your loop
while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Match found in response:", r)
        # action

# Don't forget to close the connection
tn.close()
