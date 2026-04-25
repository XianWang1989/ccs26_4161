
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Retrieve string enable settings
strings_to_search = []
for i in range(1, 4):  # Assuming you have string1, string2, string3
    string_name = f'string{i}'
    enable_name = f'{string_name}_enable'
    if config.get('Settings', enable_name) == 'yes':
        strings_to_search.append(config.get('Settings', string_name))

# Example telnet session
tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in strings_to_search):
        # Perform your action here
        print("Match found!")
