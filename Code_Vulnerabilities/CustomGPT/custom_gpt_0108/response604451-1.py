
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize Telnet connection (example)
tn = telnetlib.Telnet('your_telnet_host')

# Strings to search for
strings = ['string1', 'string2', 'string3']

# Filter enabled strings based on config
enabled_strings = [s for s in strings if config.get('SectionName', f'{s}_enable') == 'yes']

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Match found:", r)
