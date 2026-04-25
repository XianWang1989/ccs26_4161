
import ConfigParser
from telnetlib import Telnet

# Load config
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize enabled strings list
enabled_strings = []

for i in range(1, 4):  # Assuming 3 strings
    if config.get('DEFAULT', 'string{}_enable'.format(i)) == "yes":
        enabled_strings.append(config.get('DEFAULT', 'string{}'.format(i)))

# Telnet interaction
tn = Telnet('your_telnet_server')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform the desired action
        print("Match found!")
