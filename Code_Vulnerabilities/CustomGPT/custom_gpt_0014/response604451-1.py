
import telnetlib
import ConfigParser

# Load your config
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Telnet connection setup
tn = telnetlib.Telnet('your_telnet_host')

# List of strings to search based on configuration
search_strings = []

# Check which strings are enabled and add them to the search list
for i in range(1, 4):  # Assuming you have string1, string2, string3
    string_key = f'string{i}'
    enable_key = f'string{i}_enable'

    if config.get('DEFAULT', enable_key) == 'yes':
        search_strings.append(config.get('DEFAULT', string_key))

# Main loop to read and search
while True:
    r = tn.read_some()
    if any(x in r for x in search_strings):
        # Perform the desired action
        print(f'Match found: {r}')
