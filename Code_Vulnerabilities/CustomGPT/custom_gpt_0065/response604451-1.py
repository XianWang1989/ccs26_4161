
import ConfigParser
import telnetlib

# Load the configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Retrieve string enabling settings
strings = ['string1', 'string2', 'string3']
enabled_strings = [s for s in strings if config.get('DEFAULT', f'{s}_enable') == 'yes']

# Telnet connection code (replace with your actual connection details)
tn = telnetlib.Telnet('hostname', port)

# Loop to read and check for enabled strings
while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Replace with your desired action
        print("One of the enabled strings was found!")
