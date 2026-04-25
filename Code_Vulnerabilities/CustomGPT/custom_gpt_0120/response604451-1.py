
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Create a list for enabled search strings
search_strings = []
for i in range(1, 4):  # Assuming you have string1, string2, string3
    string_key = f'string{i}'
    enable_key = f'{string_key}_enable'
    if config.get(‘DEFAULT’, enable_key) == 'yes':
        search_strings.append(config.get('DEFAULT', string_key))

# Connect to telnet
tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in search_strings):
        # Perform the desired action
        print("Found one of the enabled strings!")
