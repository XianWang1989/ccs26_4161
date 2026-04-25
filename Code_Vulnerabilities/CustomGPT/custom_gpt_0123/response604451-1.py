
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Setup strings based on config
strings_to_search = []
for i in range(1, 4):  # Assuming you have string1, string2, string3
    string_key = f'string{i}'
    enable_key = f'{string_key}_enable'
    if config.get('DEFAULT', enable_key) == 'yes':
        strings_to_search.append(config.get('DEFAULT', string_key))

# Example telnet connection
tn = telnetlib.Telnet('your.telnet.server')

# Main loop
while True:
    r = tn.read_some()
    if any(x in r for x in strings_to_search):
        # Perform your action here
        print("Match found!")
