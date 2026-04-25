
import telnetlib
import ConfigParser

# Assuming 'tn' is your Telnet connection
tn = telnetlib.Telnet('your.telnet.server')

# Load config
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Create a list to hold strings to search for
search_strings = []

# Check if each string is enabled and add it to the search list
if config.get('DEFAULT', 'string1_enable') == 'yes':
    search_strings.append(config.get('DEFAULT', 'string1'))

if config.get('DEFAULT', 'string2_enable') == 'yes':
    search_strings.append(config.get('DEFAULT', 'string2'))

if config.get('DEFAULT', 'string3_enable') == 'yes':
    search_strings.append(config.get('DEFAULT', 'string3'))

while True:
    r = tn.read_some()
    if any(x in r for x in search_strings):
        # Your action here
        print("Match found!")
        # Example action
