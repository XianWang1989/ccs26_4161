
import ConfigParser
import telnetlib

# Initialize Telnet connection
tn = telnetlib.Telnet('your_telnet_host')

# Read the config file
config = ConfigParser.ConfigParser()
config.read('config.ini')

# List of strings you want to check
strings = ['string1', 'string2', 'string3']
enabled_strings = []

# Check which strings are enabled
for string in strings:
    if config.get('Settings', f'{string}_enable') == 'yes':
        enabled_strings.append(string)

# Function to search for enabled strings
while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Your action here
        print("One of the enabled strings was found!")
