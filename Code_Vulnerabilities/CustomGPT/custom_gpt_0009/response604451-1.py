
import ConfigParser
import telnetlib

# Load your config
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize strings and their enabled statuses
search_strings = [
    ('string1', config.get('settings', 'string1_enable')),
    ('string2', config.get('settings', 'string2_enable')),
    ('string3', config.get('settings', 'string3_enable'))
]

# Filter strings based on enabled status
enabled_strings = [s[0] for s in search_strings if s[1] == 'yes']

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Your action when any of the strings are found
        action
