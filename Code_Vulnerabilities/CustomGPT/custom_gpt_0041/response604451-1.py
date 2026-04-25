
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize the telnet connection (example only, modify as needed)
tn = telnetlib.Telnet('your_telnet_host')

# Strings to search
search_strings = ['string1', 'string2', 'string3']
enabled_strings = []

# Check which strings are enabled in the config
for s in search_strings:
    if config.get('SectionName', f'{s}_enable') == 'yes':
        enabled_strings.append(s)

# Read and search in a loop
while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action
        print("Match found:", r)
