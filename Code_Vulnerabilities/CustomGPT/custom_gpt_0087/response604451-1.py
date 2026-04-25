
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Define strings and their corresponding enable flags
strings = ['string1', 'string2', 'string3']
enabled_strings = [s for s in strings if config.get('DEFAULT', f'{s}_enable') == 'yes']

# Telnet connection setup
tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your desired action here
        print("Matched one of the enabled strings!")
