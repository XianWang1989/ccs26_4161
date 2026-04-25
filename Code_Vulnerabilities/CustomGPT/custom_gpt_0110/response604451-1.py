
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# List of strings to search for, along with their enable settings
search_strings = [
    ('string1', config.get('DEFAULT', 'string1_enable')),
    ('string2', config.get('DEFAULT', 'string2_enable')),
    ('string3', config.get('DEFAULT', 'string3_enable'))
]

# Filter enabled strings
enabled_strings = [s for s, enabled in search_strings if enabled.lower() == 'yes']

# Assuming tn is your Telnet connection
while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Found a match!")
