
import ConfigParser
import telnetlib

# Initialize Telnet Connection (replace with your actual connection details)
tn = telnetlib.Telnet('your.telnets.server')

# Load config
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Define your strings
strings = ['string1', 'string2', 'string3']
enabled_strings = []

# Check which strings are enabled
for s in strings:
    if config.get('Settings', f'{s}_enable') == 'yes':
        enabled_strings.append(s)

# The main loop to read from telnet
while True:
    r = tn.read_some()

    # Check if any enabled string is in the response
    if any(x in r for x in enabled_strings):
        # Perform the desired action when any enabled string is found
        print("One or more enabled strings found in the response!")
