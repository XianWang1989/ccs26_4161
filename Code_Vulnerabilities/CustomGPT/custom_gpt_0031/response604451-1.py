
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Read strings and their enabled status
strings = []
for i in range(1, 4):  # Assuming you have string1, string2, string3
    string_key = f'string{i}'
    enable_key = f'{string_key}_enable'
    if config.get('SectionName', enable_key) == 'yes':
        strings.append(config.get('SectionName', string_key))

# Telnet connection
tn = telnetlib.Telnet('hostname', port)

while True:
    r = tn.read_some()
    if any(x in r for x in strings):
        # Perform your action here
        print("Found a match!")
