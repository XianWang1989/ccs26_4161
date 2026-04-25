
import ConfigParser
from telnetlib import Telnet

# Load configuration from config.ini
config = ConfigParser.ConfigParser()
config.read('config.ini')

# List of strings to search for
strings = ['string1', 'string2', 'string3']
enabled_strings = []

# Check which strings are enabled
for string in strings:
    if config.getboolean('Settings', f'{string}_enable'):
        enabled_strings.append(string)

# Connect to the telnet server
tn = Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    # Check for any enabled string in the received data
    if any(x in r for x in enabled_strings):
        # Perform the desired action
        action()
