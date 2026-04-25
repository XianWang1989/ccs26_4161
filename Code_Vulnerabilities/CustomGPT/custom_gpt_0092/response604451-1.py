
import telnetlib
import ConfigParser  # For Python 2.7

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Establish your telnet connection
tn = telnetlib.Telnet('hostname')

# Strings to check
strings = ['string1', 'string2', 'string3']
enabled_strings = []

# Check which strings are enabled
for string in strings:
    if config.get('settings', f'{string}_enable') == 'yes':
        enabled_strings.append(string)

# Reading loop
while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Action to take if any of the enabled strings are found
        print("Found one of the enabled strings!")
        # Implement your action here
