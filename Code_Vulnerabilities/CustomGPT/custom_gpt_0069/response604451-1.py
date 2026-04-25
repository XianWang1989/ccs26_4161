
import ConfigParser
import telnetlib

# Initialize ConfigParser
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Example strings
strings_to_check = ['string1', 'string2', 'string3']
enabled_strings = []

# Check which strings are enabled
for string in strings_to_check:
    if config.get(string, 'enable') == 'yes':
        enabled_strings.append(string)

# Telnet connection
tn = telnetlib.Telnet('your.telnet.server')

# Read data loop
while True:
    r = tn.read_some()
    # Check if any enabled strings are in the response
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Found an enabled string!")
