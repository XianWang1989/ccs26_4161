
import telnetlib
import ConfigParser

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# List of strings and their enabled states
strings = [
    ('string1', config.get('Settings', 'string1_enable')),
    ('string2', config.get('Settings', 'string2_enable')),
    ('string3', config.get('Settings', 'string3_enable'))
]

# Filter to get only enabled strings
enabled_strings = [s for s, enabled in strings if enabled == 'yes']

# Connect to Telnet
tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Found a match!")

# Close the connection if needed
tn.close()
