
import ConfigParser
import telnetlib

# Load config
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Assuming string names follow a consistent naming scheme
strings = ['string1', 'string2', 'string3']
enabled_strings = []

# Collect enabled strings
for string in strings:
    if config.get(string + '_enable') == 'yes':
        enabled_strings.append(config.get(string))

# Telnet code
tn = telnetlib.Telnet('your_telnet_server')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform action when any enabled string is found
        action()
