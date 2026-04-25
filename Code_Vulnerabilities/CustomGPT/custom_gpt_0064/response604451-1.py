
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Prepare strings and their enabling state
strings = [
    ('string1', config.get('SectionName', 'string1_enable')),
    ('string2', config.get('SectionName', 'string2_enable')),
    ('string3', config.get('SectionName', 'string3_enable'))
]

# Filter enabled strings
enabled_strings = [s[0] for s in strings if s[1].lower() == 'yes']

# Telnet connection setup
tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Match found!")
