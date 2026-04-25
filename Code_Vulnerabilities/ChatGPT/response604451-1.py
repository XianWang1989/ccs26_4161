
import ConfigParser
import telnetlib

# Load your configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize your list of strings based on enabled settings
search_strings = []

# Check the status of each string enable variable
for i in range(1, 4):  # Assuming you have three strings
    if config.get('Settings', f'string{i}_enable') == 'yes':
        search_string = config.get('Settings', f'string{i}')
        search_strings.append(search_string)

# Create your Telnet connection
tn = telnetlib.Telnet('your_telnet_host', 23)  # Adjust host and port as necessary

# Your original loop modified with the dynamically created search string list
while True:
    r = tn.read_some()
    if any(x in r for x in search_strings):
        action  # Implement your action here
