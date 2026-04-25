
import telnetlib
import ConfigParser

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Read strings and their enable status
strings = [
    ('string1', config.get('Settings', 'string1_enable')),
    ('string2', config.get('Settings', 'string2_enable')),
    ('string3', config.get('Settings', 'string3_enable')),
]

# Filter enabled strings
enabled_strings = [s[0] for s in strings if s[1] == 'yes']

with telnetlib.Telnet('hostname') as tn:
    while True:
        r = tn.read_some()
        if any(x in r for x in enabled_strings):
            # Perform your action here
            print("Action performed for:", ", ".join(enabled_strings))
