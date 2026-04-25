
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Strings to search for
search_strings = []

# Check which strings to include based on config
if config.get('settings', 'string1_enable') == "yes":
    search_strings.append(config.get('settings', 'string1'))
if config.get('settings', 'string2_enable') == "yes":
    search_strings.append(config.get('settings', 'string2'))
if config.get('settings', 'string3_enable') == "yes":
    search_strings.append(config.get('settings', 'string3'))

# Telnet setup
tn = telnetlib.Telnet('hostname')

# Continuous read loop
while True:
    r = tn.read_some()
    if any(x in r for x in search_strings):
        print("Match found! Executing action...")
        # Place your action code here
