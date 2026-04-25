
import telnetlib
import ConfigParser

# Load configurations
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize telnet connection
tn = telnetlib.Telnet('your_telnet_host')

# Get enabled strings
enabled_strings = []
for i in range(1, 4):  # Assuming you have 3 strings
    if config.get('Settings', f'string{i}_enable') == 'yes':
        enabled_strings.append(config.get('Settings', f'string{i}'))

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action
        print("Found an active string!")
