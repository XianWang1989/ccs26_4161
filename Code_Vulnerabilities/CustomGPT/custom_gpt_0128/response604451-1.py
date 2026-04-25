
import telnetlib
import ConfigParser

# Load config settings
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Get strings and their statuses
strings = [
    (config.get('Settings', 'string1'), config.get('Settings', 'string1_enable')),
    (config.get('Settings', 'string2'), config.get('Settings', 'string2_enable')),
    (config.get('Settings', 'string3'), config.get('Settings', 'string3_enable')),
]

# Filter for enabled strings
enabled_strings = [s for s, enabled in strings if enabled == 'yes']

tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Match found!")

