
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Retrieve strings and their enable statuses
strings = ['string1', 'string2', 'string3']  # Add more strings as needed
enabled_strings = [s for s in strings if config.get(s + '_enable', 'no') == 'yes']

# Connect to Telnet
tn = telnetlib.Telnet('hostname')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Implement your action here
        print("Found one of the enabled strings!")
