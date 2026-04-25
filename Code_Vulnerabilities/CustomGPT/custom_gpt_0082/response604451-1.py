
import ConfigParser
import telnetlib

# Load the config file
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize the Telnet connection
tn = telnetlib.Telnet('your_telnet_host')

# List of strings to search for
strings = ['string1', 'string2', 'string3']

# Building the enabled strings list
enabled_strings = [s for s in strings if config.get('DEFAULT', f'{s}_enable') == 'yes']

while True:
    r = tn.read_some()

    # Check for any enabled strings in the response
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Found an enabled string!")
