
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize Telnet
tn = telnetlib.Telnet('your_telnet_host')

# Define your strings
strings = ['string1', 'string2', 'string3']
enabled_strings = []

# Check which strings are enabled
for s in strings:
    if config.get('section_name', f'{s}_enable') == 'yes':
        enabled_strings.append(s)

# Main loop to read from telnet
while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        action()
