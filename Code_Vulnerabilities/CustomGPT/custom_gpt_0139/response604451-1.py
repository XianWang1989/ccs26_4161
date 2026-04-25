
import ConfigParser
import telnetlib

# Assuming you have a config.ini file structured appropriately
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize your Telnet connection
tn = telnetlib.Telnet('hostname', port)

# Create a list of strings to check based on the config file
strings_to_check = {
    'string1': config.get('Settings', 'string1_enable'),
    'string2': config.get('Settings', 'string2_enable'),
    'string3': config.get('Settings', 'string3_enable')
}

# Infinite loop to read from telnet
while True:
    r = tn.read_some()

    # Create a list of active strings based on their enabled status
    active_strings = [key for key, value in strings_to_check.items() if value.lower() == 'yes']

    # Check if any of the enabled strings are in the response
    if any(x in r for x in active_strings):
        # Execute your desired action
        print("Match found: ", [x for x in active_strings if x in r])
