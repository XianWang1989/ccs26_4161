
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Retrieve strings and their enable status
strings = [
    ('string1', config.get('Section', 'string1_enable')),
    ('string2', config.get('Section', 'string2_enable')),
    ('string3', config.get('Section', 'string3_enable'))
]

# Filter for enabled strings
enabled_strings = [s[0] for s in strings if s[1] == 'yes']

# Telnet connection
tn = telnetlib.Telnet('hostname', port)

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform the desired action here
        print("Matched one of the enabled strings:", r)
