
import telnetlib
import ConfigParser

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Example strings
strings = {
    'string1': config.get('DEFAULT', 'string1'),
    'string2': config.get('DEFAULT', 'string2'),
    'string3': config.get('DEFAULT', 'string3')
}

# Enable status
enabled = {
    'string1': config.get('DEFAULT', 'string1_enable') == 'yes',
    'string2': config.get('DEFAULT', 'string2_enable') == 'yes',
    'string3': config.get('DEFAULT', 'string3_enable') == 'yes'
}

# Connect to Telnet
tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    # Check for enabled strings
    active_strings = [s for s in strings if enabled[s]]

    if any(s in r for s in active_strings):
        # Perform your action
        print("Found a match!")
