
import telnetlib
import ConfigParser

# Read configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Strings to search
strings_to_search = ['string1', 'string2', 'string3']
enabled_strings = [s for s in strings_to_search if config.get('Settings', f'{s}_enable') == 'yes']

# Connecting to the Telnet server
tn = telnetlib.Telnet('hostname', port)

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Matched one of the strings:", r)
