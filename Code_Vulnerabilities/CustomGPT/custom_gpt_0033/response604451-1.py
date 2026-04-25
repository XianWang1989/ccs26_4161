
import ConfigParser
import telnetlib

# Read the config file
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize telnet connection
tn = telnetlib.Telnet('your.telnet.server')

# Define your strings and their enabling status
strings_to_search = [string1, string2, string3]
enabled_strings = [s for s in strings_to_search if config.get('Settings', f'{s}_enable') == 'yes']

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action
        print("Match found!")
