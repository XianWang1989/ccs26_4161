
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Define the strings and their corresponding enable flags
strings = [
    ('string1', config.get('Settings', 'string1_enable')),
    ('string2', config.get('Settings', 'string2_enable')),
    ('string3', config.get('Settings', 'string3_enable'))
]

# Filter enabled strings
enabled_strings = [s for s, enabled in strings if enabled == 'yes']

# Telnet connection setup (example)
tn = telnetlib.Telnet('your.telnet.server')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Match found in:", r)
