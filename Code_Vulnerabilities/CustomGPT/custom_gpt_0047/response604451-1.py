
import ConfigParser
from telnetlib import Telnet

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Sample strings
string1 = "example1"
string2 = "example2"
string3 = "example3"

# Prepare list of enabled strings
enabled_strings = []

if config.get('DEFAULT', 'string1_enable') == "yes":
    enabled_strings.append(string1)
if config.get('DEFAULT', 'string2_enable') == "yes":
    enabled_strings.append(string2)
if config.get('DEFAULT', 'string3_enable') == "yes":
    enabled_strings.append(string3)

# Connect to telnet
tn = Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Found one of the strings!")
