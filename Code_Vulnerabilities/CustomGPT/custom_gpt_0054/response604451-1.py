
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.RawConfigParser()
config.read('config.ini')

# Initialize telnet connection
tn = telnetlib.Telnet('hostname')

# Gather enabled strings
enabled_strings = []
for i in range(1, 4):  # Assuming you have string1, string2, string3
    string_key = f'string{i}'
    enable_key = f'{string_key}_enable'
    if config.get('section_name', enable_key) == 'yes':  # replace 'section_name' with your actual section in config.ini
        enabled_strings.append(config.get('section_name', string_key))

# Read response and check for enabled strings
while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform some action
        print("Match found!")
