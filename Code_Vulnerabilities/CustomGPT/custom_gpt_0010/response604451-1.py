
import ConfigParser
import telnetlib

# Load the configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize Telnet connection
tn = telnetlib.Telnet('your_telnet_host')

# Define strings to check
strings = ['string1', 'string2', 'string3']
enabled_strings = []

# Check which strings are enabled based on the config
for string in strings:
    if config.get('settings', f'{string}_enable') == 'yes':
        enabled_strings.append(string)

while True:
    r = tn.read_some()

    # Check if any enabled string appears in the response
    if any(x in r for x in enabled_strings):
        # Perform your desired action here
        print("Found an enabled string!")
