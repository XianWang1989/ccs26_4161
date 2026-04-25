
import telnetlib
import ConfigParser  # For Python 2.7

# Load your configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Retrieve enabled strings
enabled_strings = []
for i in range(1, 4):  # Assuming you're checking string1, string2, string3
    if config.get('Settings', f'string{i}_enable') == 'yes':
        enabled_strings.append(config.get('Settings', f'string{i}'))

# Start Telnet connection
tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Match found!")

# Remember to replace 'your_telnet_host' with the actual hostname.
