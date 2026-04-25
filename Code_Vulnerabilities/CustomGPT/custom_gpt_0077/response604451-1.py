
import ConfigParser
import telnetlib

# Load your configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Define the strings to check
strings = ['string1', 'string2', 'string3']
enabled_strings = []

# Collect enabled strings
for string in strings:
    if config.get('DEFAULT', f'{string}_enable') == 'yes':
        enabled_strings.append(string)

# Telnet connection (assuming 'tn' is your Telnet connection object)
while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Match found!")
