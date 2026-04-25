
import telnetlib
import ConfigParser

# Read from the config.ini file
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Define strings and their enabled statuses
search_strings = [
    ('string1', config.get('Settings', 'string1_enable')),
    ('string2', config.get('Settings', 'string2_enable')),
    ('string3', config.get('Settings', 'string3_enable'))
]

# Filter enabled strings
enabled_strings = [s[0] for s in search_strings if s[1] == 'yes']

tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action
        print("Match found!")
