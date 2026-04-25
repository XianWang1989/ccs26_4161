
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Fetch enabled strings based on configuration
enabled_strings = []
for i in range(1, 4):  # Adjust for the number of strings you're using
    if config.get('Settings', f'string{i}_enable') == 'yes':
        enabled_strings.append(config.get('Settings', f'string{i}'))

# Telnet connection setup
tn = telnetlib.Telnet('your_telnet_host')  # Replace with actual host

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action when any of the enabled strings is found
        print("Enabled string found!")
