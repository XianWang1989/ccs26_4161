
import ConfigParser
import telnetlib

# Read configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize your strings
strings = ['string1', 'string2', 'string3']
enabled_strings = []

# Check which strings are enabled
for s in strings:
    if config.getboolean(s + '_enable'):
        enabled_strings.append(s)

# Connect to the Telnet server (example)
tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Action if any strings are found
        print("Match found!")
