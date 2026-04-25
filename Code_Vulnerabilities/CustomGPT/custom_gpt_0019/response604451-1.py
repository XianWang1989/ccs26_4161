
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Define the strings and their enable states
strings = [
    ('string1', config.get('SectionName', 'string1_enable')),
    ('string2', config.get('SectionName', 'string2_enable')),
    ('string3', config.get('SectionName', 'string3_enable')),
]

# Filter the enabled strings
enabled_strings = [s[0] for s in strings if s[1] == 'yes']

# Start telnet session
tn = telnetlib.Telnet('hostname', port)

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Match found!")
