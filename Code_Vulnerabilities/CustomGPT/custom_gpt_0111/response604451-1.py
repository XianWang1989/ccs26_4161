
import telnetlib
import ConfigParser

# Load the configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize the telnet connection
tn = telnetlib.Telnet('your_telnet_server')

# Strings and their corresponding enable settings
strings_to_check = ['string1', 'string2', 'string3']
enabled_strings = [s for s in strings_to_check if config.get('Settings', f'{s}_enable') == 'yes']

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Take necessary action here
        print("Match found in response.")
