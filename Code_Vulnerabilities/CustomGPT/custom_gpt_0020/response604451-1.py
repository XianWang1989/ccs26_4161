
import ConfigParser
import telnetlib

# Read the configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize strings and their statuses
strings_to_search = []
if config.get('Settings', 'string1_enable') == 'yes':
    strings_to_search.append(config.get('Settings', 'string1'))
if config.get('Settings', 'string2_enable') == 'yes':
    strings_to_search.append(config.get('Settings', 'string2'))
if config.get('Settings', 'string3_enable') == 'yes':
    strings_to_search.append(config.get('Settings', 'string3'))

# Assuming `tn` is your telnet connection
while True:
    r = tn.read_some()
    if any(x in r for x in strings_to_search):
        # Perform the desired action
        print("Matched String Found!")
