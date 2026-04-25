
import ConfigParser
import telnetlib

# Load configuration from config.ini
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Retrieve the strings and their enabled status from the config
strings = [
    (config.get('DEFAULT', 'string1'), config.get('DEFAULT', 'string1_enable')),
    (config.get('DEFAULT', 'string2'), config.get('DEFAULT', 'string2_enable')),
    (config.get('DEFAULT', 'string3'), config.get('DEFAULT', 'string3_enable')),
]

# Create a list of enabled strings
enabled_strings = [s for s, enabled in strings if enabled.lower() == 'yes']

# Connect to Telnet
tn = telnetlib.Telnet('your_telnet_server')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Match found!")
