
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Define your strings
enabled_strings = []
if config.get('settings', 'string1_enable') == "yes":
    enabled_strings.append(config.get('settings', 'string1'))
if config.get('settings', 'string2_enable') == "yes":
    enabled_strings.append(config.get('settings', 'string2'))
if config.get('settings', 'string3_enable') == "yes":
    enabled_strings.append(config.get('settings', 'string3'))

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        action  # Replace with your desired action
