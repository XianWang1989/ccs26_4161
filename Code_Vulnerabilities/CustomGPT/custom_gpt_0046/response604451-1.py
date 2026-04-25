
import ConfigParser
import telnetlib

# Load the configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Read enabled strings
strings_to_check = []
for i in range(1, 4):  # Assuming you have configurations for string1, string2, string3
    string_key = f'string{i}'
    enabled_key = f'{string_key}_enable'
    if config.get('DEFAULT', enabled_key) == "yes":
        strings_to_check.append(config.get('DEFAULT', string_key))

# Telnet connection setup
tn = telnetlib.Telnet('your_telnet_host', your_telnet_port)

while True:
    r = tn.read_some()
    if any(x in r for x in strings_to_check):
        # Perform your action here
        print("Match found!")
