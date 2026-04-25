
import ConfigParser
import telnetlib

# Read configuration from config.ini
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize the telnet connection
tn = telnetlib.Telnet('hostname', port)

# List to hold active strings
search_strings = []

# Check enabled strings in the config and add to the search list
for i in range(1, 4):  # Assuming you have string1, string2, string3
    string_name = f'string{i}'
    enable_key = f'{string_name}_enable'

    if config.get('DEFAULT', enable_key) == 'yes':
        search_strings.append(config.get('DEFAULT', string_name))

# Search for the enabled strings
while True:
    r = tn.read_some()
    if any(x in r for x in search_strings):
        # Action you want to perform
        print("Match found!")
