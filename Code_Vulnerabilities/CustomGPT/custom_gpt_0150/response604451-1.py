
import ConfigParser
import telnetlib

# Read configurations
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize the telnet connection
tn = telnetlib.Telnet('your_telnet_host')

# Prepare the search strings based on their enabled status
search_strings = []
for i in range(1, 4):  # Assuming you have string1, string2, ..., string3
    string_key = f'string{i}'
    enable_key = f'{string_key}_enable'
    if config.get('Section', enable_key) == 'yes':
        search_strings.append(config.get('Section', string_key))

# Read and search in a loop
while True:
    r = tn.read_some()
    if any(x in r for x in search_strings):
        # Perform your action here
        print("Found a match!")
