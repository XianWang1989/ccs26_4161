
import ConfigParser
import telnetlib

# Load configurations
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Retrieve strings and their enable statuses
enabled_strings = []
for i in range(1, 4):  # Assuming you have string1, string2, string3
    string_key = f'string{i}'
    enable_key = f'{string_key}_enable'
    if config.get(‘DEFAULT’, enable_key) == "yes":
        enabled_strings.append(config.get('DEFAULT', string_key))

# Telnet connection setup
tn = telnetlib.Telnet('host', port)

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Match found!")
