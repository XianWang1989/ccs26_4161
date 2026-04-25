
import ConfigParser
import telnetlib

# Load the configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Strings to check
strings = ['string1', 'string2', 'string3']
enabled_strings = []

# Check enable/disable status
for string in strings:
    if config.get('Settings', f'{string}_enable') == 'yes':
        enabled_strings.append(string)

# Telnet connection setup
tn = telnetlib.Telnet('hostname', port)

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform the action if any enabled string is found
        action()
