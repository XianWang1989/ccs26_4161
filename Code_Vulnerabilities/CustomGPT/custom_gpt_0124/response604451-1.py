
import telnetlib
import ConfigParser

# Read the config
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Setup the telnet connection
tn = telnetlib.Telnet('your_telnet_host')

# Define the strings to search for and their corresponding configuration keys
search_strings = ['string1', 'string2', 'string3']
enable_keys = ['string1_enable', 'string2_enable', 'string3_enable']

# Gather the enabled strings
enabled_strings = [s for s, key in zip(search_strings, enable_keys) if config.get('DEFAULT', key) == 'yes']

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Matching string found!")

# Don't forget to close the connection (optional, based on your use case)
tn.close()
