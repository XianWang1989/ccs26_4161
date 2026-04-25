
import ConfigParser
import telnetlib

# Assuming you have a ConfigParser setup for your config.ini
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize your strings and their corresponding enable states
strings = [
    ('string1', config.get('Settings', 'string1_enable')),
    ('string2', config.get('Settings', 'string2_enable')),
    ('string3', config.get('Settings', 'string3_enable')),
    # Add more strings as needed
]

# Filter enabled strings
enabled_strings = [s for s, enabled in strings if enabled == "yes"]

tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Found one of the enabled strings.")
