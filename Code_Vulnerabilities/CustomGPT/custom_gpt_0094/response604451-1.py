
import ConfigParser
from telnetlib import Telnet

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Assuming the strings are defined as follows
string1 = "search_string_1"
string2 = "search_string_2"
string3 = "search_string_3"

# Get the enable/disable states from the config
enabled_strings = []
if config.get('section_name', 'string1_enable') == 'yes':
    enabled_strings.append(string1)
if config.get('section_name', 'string2_enable') == 'yes':
    enabled_strings.append(string2)
if config.get('section_name', 'string3_enable') == 'yes':
    enabled_strings.append(string3)

# Initialize Telnet connection (assume tn is your Telnet object)
tn = Telnet('your_telnet_server')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Matching string found!")
