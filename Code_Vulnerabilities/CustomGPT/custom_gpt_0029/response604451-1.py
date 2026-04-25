
import ConfigParser
import telnetlib

# Load the config
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize variables
enabled_strings = []

# Check which strings are enabled
for i in range(1, 4):  # Assuming you have string1, string2, string3
    string_name = f'string{i}'
    enabled = config.get('DEFAULT', f'{string_name}_enable')
    if enabled.lower() == 'yes':
        enabled_strings.append(config.get('DEFAULT', string_name))

# Telnet connection (example)
tn = telnetlib.Telnet('hostname')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Your action here
        print("Matched Strings Found")
