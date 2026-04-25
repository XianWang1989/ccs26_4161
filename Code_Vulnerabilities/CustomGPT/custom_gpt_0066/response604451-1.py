
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Prepare the strings and their enabled states
search_strings = []
for i in range(1, 4):  # Assuming you have string1, string2, string3
    string_key = f'string{i}'
    enable_key = f'{string_key}_enable'
    if config.get(enable_key, 'no') == 'yes':
        search_strings.append(config.get(string_key))

# Telnet connection code here
tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in search_strings):
        # Perform your action here
        print("Match found!")
