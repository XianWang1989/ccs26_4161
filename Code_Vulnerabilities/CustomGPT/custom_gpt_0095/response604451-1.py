
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Define your strings
strings = ['string1', 'string2', 'string3']
enabled_strings = []

# Check which strings are enabled
for string in strings:
    if config.get('Settings', f'{string}_enable') == 'yes':
        enabled_strings.append(string)

# Telnet connection setup
tn = telnetlib.Telnet('your.telnet.server')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Match found!")
