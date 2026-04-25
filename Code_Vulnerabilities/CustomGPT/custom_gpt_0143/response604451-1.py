
import ConfigParser
import telnetlib

# Read the configuration file
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize the telnet connection
tn = telnetlib.Telnet('hostname', port)

# List of strings to check
strings = ['string1', 'string2', 'string3']
enabled_search_strings = []

# Check enabled statuses and add to the search list
for s in strings:
    if config.get('Settings', f'{s}_enable') == 'yes':
        enabled_search_strings.append(s)

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_search_strings):
        # Perform your action here
        print("Found one of the enabled strings!")
