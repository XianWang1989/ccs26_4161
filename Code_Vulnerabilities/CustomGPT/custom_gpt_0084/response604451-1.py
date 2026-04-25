
import ConfigParser
import telnetlib

# Load config file
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize telnet connection
tn = telnetlib.Telnet('hostname', 23)  # replace 'hostname' with your actual host

# List to hold enabled strings
enabled_strings = []

# Check which strings are enabled
for i in range(1, 4):  # assuming you have string1, string2, string3
    string_key = f'string{i}'
    enable_key = f'{string_key}_enable'

    if config.get('DEFAULT', enable_key) == 'yes':
        enabled_strings.append(config.get('DEFAULT', string_key))

# Reading incoming data
while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action
        print("Matched:", r)
