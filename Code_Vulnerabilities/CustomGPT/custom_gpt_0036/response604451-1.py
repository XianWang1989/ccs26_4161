
import telnetlib
import ConfigParser

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Setup your strings and their enabling flags
strings_to_check = ['string1', 'string2', 'string3']
enabled_strings = []

for string in strings_to_check:
    if config.get(string, 'enable') == 'yes':
        enabled_strings.append(config.get(string, 'value'))

# Connect to your telnet server
tn = telnetlib.Telnet('your_telnet_server')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Execute your action here based on the matched string
        print("Match found: ", [x for x in enabled_strings if x in r])
