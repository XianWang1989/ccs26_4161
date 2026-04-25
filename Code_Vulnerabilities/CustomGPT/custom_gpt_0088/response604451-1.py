
import ConfigParser
import telnetlib

# Load the configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Get enabled strings
enabled_strings = []
for i in range(1, 4):  # Assuming up to 3 strings
    string_name = f'string{i}'
    enable_name = f'string{i}_enable'
    if config.get(enable_name) == 'yes':
        enabled_strings.append(config.get(string_name))

# Telnet setup
tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Matched:", r)
