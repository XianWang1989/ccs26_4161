
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize Telnet session
tn = telnetlib.Telnet('your_telnet_host')

# Prepare the list based on config
search_strings = []
for i in range(1, 4):  # Assuming you have string1, string2, string3
    string_key = f'string{i}'
    enabled_key = f'{string_key}_enable'
    if config.get('your_section', enabled_key) == 'yes':
        search_strings.append(config.get('your_section', string_key))

while True:
    r = tn.read_some()
    if any(x in r for x in search_strings):
        # Perform your action
        print("Match found!")
