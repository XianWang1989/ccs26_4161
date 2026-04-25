
import ConfigParser
import telnetlib

# Load the configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Assuming the strings to search for are defined like this in your config.ini:
# [Strings]
# string1 = your_string1
# string1_enable = yes
# string2 = your_string2
# string2_enable = no
# string3 = your_string3
# string3_enable = yes

# Retrieve strings and their enabled statuses
strings_to_search = []
for i in range(1, 4):  # Adjust based on how many strings you have
    string_key = f'string{i}'
    enable_key = f'string{i}_enable'

    if config.getboolean('Strings', enable_key):  # This returns True for 'yes', False for 'no'
        strings_to_search.append(config.get('Strings', string_key))

# Telnet connection setup (replace with actual host and port)
tn = telnetlib.Telnet('your_telnet_host', port)

while True:
    r = tn.read_some()
    if any(x in r for x in strings_to_search):
        # Action to take when one of the strings is found
        print("Found a string!")
        # Implement your action here
