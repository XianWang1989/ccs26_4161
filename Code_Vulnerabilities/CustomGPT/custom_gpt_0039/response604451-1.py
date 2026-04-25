
import configparser
import telnetlib

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Initialize telnet connection
tn = telnetlib.Telnet('your.telnet.server')

# Define the strings based on the configuration
enabled_strings = []
if config.get('Settings', 'string1_enable') == 'yes':
    enabled_strings.append(config.get('Settings', 'string1'))
if config.get('Settings', 'string2_enable') == 'yes':
    enabled_strings.append(config.get('Settings', 'string2'))
if config.get('Settings', 'string3_enable') == 'yes':
    enabled_strings.append(config.get('Settings', 'string3'))

# Continuous reading loop
while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Take action if any string is found
        print("Match found!")
        # Perform your action here
