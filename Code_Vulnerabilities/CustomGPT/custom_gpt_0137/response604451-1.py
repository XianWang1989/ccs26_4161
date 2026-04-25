
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Fetch strings and their enabled status from the config
strings_to_search = []
for i in range(1, 4):  # Assuming you have three strings: string1, string2, string3
    string_name = f'string{i}'
    enabled_key = f'{string_name}_enable'

    # Check if the string is enabled
    if config.get('DEFAULT', enabled_key) == "yes":
        strings_to_search.append(config.get('DEFAULT', string_name))

tn = telnetlib.Telnet('hostname', port)  # Update with the actual hostname and port

while True:
    r = tn.read_some()
    if any(x in r for x in strings_to_search):
        # Perform your action here
        print("Found a matching string in the response!")
