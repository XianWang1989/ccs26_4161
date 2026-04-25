
import telnetlib
import configparser

# Read configuration from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# List of strings and their enabled status
strings_to_check = {
    'string1': config.get('Settings', 'string1_enable'),
    'string2': config.get('Settings', 'string2_enable'),
    'string3': config.get('Settings', 'string3_enable')
}

# Initialize telnet connection
tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()

    # Build a list of strings to check based on their enabled status
    active_strings = [string for string, enabled in strings_to_check.items() if enabled == 'yes']

    # Check if any of the active strings are in the response
    if any(x in r for x in active_strings):
        # Perform your action here
        print("Found a match!")
