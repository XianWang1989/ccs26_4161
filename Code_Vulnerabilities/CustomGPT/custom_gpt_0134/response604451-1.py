
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Retrieve strings and their enable status
strings = ['string1', 'string2', 'string3']
enabled_strings = [s for s in strings if config.get('DEFAULT', f'{s}_enable') == 'yes']

# Telnet connection setup
tn = telnetlib.Telnet('hostname')  # Replace 'hostname' with your Telnet server

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print(f'Matched: {", ".join(enabled_strings)}')
