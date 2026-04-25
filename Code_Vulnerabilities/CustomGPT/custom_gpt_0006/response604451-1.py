
import telnetlib
import ConfigParser

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Retrieve strings and their enabled status
strings = [
    (config.get('Settings', 'string1'), config.get('Settings', 'string1_enable')),
    (config.get('Settings', 'string2'), config.get('Settings', 'string2_enable')),
    (config.get('Settings', 'string3'), config.get('Settings', 'string3_enable'))
]

tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()

    # Create a list of enabled strings
    enabled_strings = [s for s, enabled in strings if enabled.lower() == 'yes']

    # Check if any enabled string is in the response
    if any(s in r for s in enabled_strings):
        # Perform your action here
        print('Match found! Performing action...')
