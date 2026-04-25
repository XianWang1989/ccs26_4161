
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Strings and their enabled status
strings = [
    ('string1', config.get('DEFAULT', 'string1_enable')),
    ('string2', config.get('DEFAULT', 'string2_enable')),
    ('string3', config.get('DEFAULT', 'string3_enable'))
]

# Filter enabled strings
enabled_strings = [s[0] for s in strings if s[1] == 'yes']

# Start telnet session
tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action
        print("Match found:", [x for x in enabled_strings if x in r])
