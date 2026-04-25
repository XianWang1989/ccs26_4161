
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize Telnet connection (assuming 'tn' is your Telnet object)
tn = telnetlib.Telnet('your_telnet_host')

# Define strings
strings = ['string1', 'string2', 'string3']

# Get enabled strings from config
enabled_strings = [s for s in strings if config.get('Settings', f"{s}_enable") == 'yes']

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform action
        pass  # Replace with your action code
