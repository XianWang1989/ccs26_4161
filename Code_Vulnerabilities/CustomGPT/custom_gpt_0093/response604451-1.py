
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# List of strings to search with their corresponding enabled status
strings_to_search = ['string1', 'string2', 'string3']
enabled_strings = [s for s in strings_to_search if config.get('DEFAULT', f'{s}_enable') == 'yes']

# Telnet connection
tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Action when any enabled string is found
        print("Found a match!")
