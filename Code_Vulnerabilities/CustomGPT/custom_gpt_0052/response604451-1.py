
import ConfigParser
from telnetlib import Telnet

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize telnet
tn = Telnet('your_telnet_host')

# Strings and their enable flags
search_strings = []
for i in range(1, 4):  # Assuming you have up to 3 strings
    string = config.get('SectionName', 'string{}'.format(i))
    enabled = config.get('SectionName', 'string{}_enable'.format(i))

    if enabled.lower() == 'yes':
        search_strings.append(string)

while True:
    r = tn.read_some()
    if any(x in r for x in search_strings):
        # Perform action if any enabled string is found
        print("Found a match!")
