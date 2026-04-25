
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Establish telnet connection
tn = telnetlib.Telnet('your_telnet_host')

# Prepare strings based on the config
search_strings = [s for s in ['string1', 'string2', 'string3'] 
                  if config.get('Settings', f'{s}_enable') == 'yes']

# Read data and search for enabled strings
while True:
    r = tn.read_some()
    if any(x in r for x in search_strings):
        # Perform action if any enabled string is found
        action()
