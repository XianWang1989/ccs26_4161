
import telnetlib
import ConfigParser

# Load the configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Connect to the Telnet server
tn = telnetlib.Telnet('your_telnet_server')

# Define the strings to search for
strings_to_search = ['string1', 'string2', 'string3']
enabled_strings = []

# Check which strings are enabled
for s in strings_to_search:
    if config.get('DEFAULT', f'{s}_enable') == 'yes':
        enabled_strings.append(s)

# Continuously read from Telnet
while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Action to take when one of the strings is found
        print("Found one of the enabled strings!")
