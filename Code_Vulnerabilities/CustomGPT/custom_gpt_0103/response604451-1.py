
import ConfigParser
import telnetlib

# Setup Telnet
tn = telnetlib.Telnet('your_telnet_host')

# Read the config file
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Define strings and their corresponding config keys
strings = ['string1', 'string2', 'string3']
enabled_strings = []

# Check which strings are enabled
for string in strings:
    if config.get(string, 'enable') == 'yes':
        enabled_strings.append(string)

while True:
    r = tn.read_some()

    # Check if any enabled string is in the response
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Match found for:", enabled_strings)
