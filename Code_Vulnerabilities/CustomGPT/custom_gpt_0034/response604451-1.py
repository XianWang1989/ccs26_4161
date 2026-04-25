
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Read enabled/disabled statuses
enabled_strings = []
for i in range(1, 4):  # Assuming you have string1, string2, string3
    if config.get('Settings', f'string{i}_enable') == 'yes':
        enabled_strings.append(config.get('Settings', f'string{i}'))

# Telnet setup
tn = telnetlib.Telnet('your_telnet_host')  # Replace with your Telnet host

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform action if any enabled string is found
        print("Match found! Performing action...")
        # Your action code here
