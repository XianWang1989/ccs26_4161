
import ConfigParser
import telnetlib

# Read configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Fetch enabled strings
search_strings = []
if config.get('Settings', 'string1_enable') == 'yes':
    search_strings.append(config.get('Settings', 'string1'))
if config.get('Settings', 'string2_enable') == 'yes':
    search_strings.append(config.get('Settings', 'string2'))
if config.get('Settings', 'string3_enable') == 'yes':
    search_strings.append(config.get('Settings', 'string3'))

# Telnet connection
tn = telnetlib.Telnet('hostname', port)

# Searching loop
while True:
    r = tn.read_some()
    if any(x in r for x in search_strings):
        # Perform action if any string is found
        print("Match found!")
        # action here
