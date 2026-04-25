
import ConfigParser
from telnetlib import Telnet

# Load the configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Define the strings and their corresponding enable flags
strings = ['string1', 'string2', 'string3']
enabled_strings = [string for string in strings if config.get('Settings', f'{string}_enable') == 'yes']

tn = Telnet('your_telnet_server')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Action triggered for: ", [x for x in enabled_strings if x in r])
