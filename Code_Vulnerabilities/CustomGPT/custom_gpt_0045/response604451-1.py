
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Read enabled strings from config
enabled_strings = []
for i in range(1, 4):  # Assuming you have three strings to check (string1, string2, string3)
    string_enable_key = f'string{i}_enable'
    string_key = f'string{i}'
    if config.get('SectionName', string_enable_key) == 'yes':  # Adjust 'SectionName' appropriately
        enabled_strings.append(config.get('SectionName', string_key))

# Telnet connection example
tn = telnetlib.Telnet('hostname')  # Replace 'hostname' with your telnet server address

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        action = "Found a match!"  # Replace with your actual action
        print(action)
