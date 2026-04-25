
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Get enabled strings
strings_to_search = []
if config.get('SectionName', 'string1_enable') == "yes":
    strings_to_search.append(config.get('SectionName', 'string1'))
if config.get('SectionName', 'string2_enable') == "yes":
    strings_to_search.append(config.get('SectionName', 'string2'))
if config.get('SectionName', 'string3_enable') == "yes":
    strings_to_search.append(config.get('SectionName', 'string3'))

# Telnet connection setup
tn = telnetlib.Telnet('your_telnet_server')

# Searching for enabled strings
while True:
    r = tn.read_some()
    if any(x in r for x in strings_to_search):
        # Perform desired action
        print("Match found:", r)
