
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Retrieve strings and their enabled statuses
strings_to_search = [
    ('string1', config.get('Settings', 'string1_enable')),
    ('string2', config.get('Settings', 'string2_enable')),
    ('string3', config.get('Settings', 'string3_enable')),
]

# Create a list of enabled strings
enabled_strings = [s[0] for s in strings_to_search if s[1] == 'yes']

# Start telnet session
tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your desired action
        print("Found a match!")
