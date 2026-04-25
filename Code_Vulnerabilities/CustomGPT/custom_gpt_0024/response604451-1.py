
import telnetlib
import ConfigParser

# Load the configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Retrieve the strings and their enable status
strings = []
for i in range(1, 4):  # Assuming you have 3 strings
    string_key = f'string{i}'
    enable_key = f'string{i}_enable'
    if config.get(enable_key) == 'yes':
        strings.append(config.get(string_key))

# Telnet connection
tn = telnetlib.Telnet('hostname', port)

while True:
    r = tn.read_some()
    if any(x in r for x in strings):
        # Perform your action here
        print("Match found!")
