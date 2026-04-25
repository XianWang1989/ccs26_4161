
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize your strings and their enable flags
search_strings = []
for i in range(1, 4):
    string_name = f'string{i}'
    enable_name = f'string{i}_enable'
    if config.get('Settings', enable_name) == 'yes':
        search_strings.append(config.get('Settings', string_name))

# Telnet connection (Make sure to replace with your actual host and port)
tn = telnetlib.Telnet('your_telnet_host', your_port_here)

# Read from telnet
while True:
    r = tn.read_some()
    if any(x in r for x in search_strings):
        # Your action when at least one string is found
        print("Match found!")
