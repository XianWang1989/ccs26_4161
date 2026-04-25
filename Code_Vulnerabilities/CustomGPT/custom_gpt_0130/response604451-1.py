
import ConfigParser
import telnetlib

# Read configuration settings
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Define your strings and their corresponding enable flags
strings = ['string1', 'string2', 'string3']
enabled_strings = []

for s in strings:
    if config.get('DEFAULT', f'{s}_enable') == 'yes':
        enabled_strings.append(s)

# Telnet connection
tn = telnetlib.Telnet('hostname', port)  # specify your Telnet connection details

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Found a match!")
