
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Read enabled strings from config
enabled_strings = []
if config.get('section', 'string1_enable') == 'yes':
    enabled_strings.append(config.get('section', 'string1'))

if config.get('section', 'string2_enable') == 'yes':
    enabled_strings.append(config.get('section', 'string2'))

if config.get('section', 'string3_enable') == 'yes':
    enabled_strings.append(config.get('section', 'string3'))

# Assuming you have established a Telnet connection as tn
while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Execute your action here
        print("Match found!")
