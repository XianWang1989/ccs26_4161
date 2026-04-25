
import ConfigParser
from telnetlib import Telnet

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Assuming these are the strings you want to search for
strings_to_search = {
    'string1': config.get('Settings', 'string1_enable'),
    'string2': config.get('Settings', 'string2_enable'),
    'string3': config.get('Settings', 'string3_enable'),
}

# Create a list of enabled strings
enabled_strings = [key for key, value in strings_to_search.items() if value == 'yes']

# Initialize Telnet connection
tn = Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Implement the action you want to take here
        print("Match found:", r)
