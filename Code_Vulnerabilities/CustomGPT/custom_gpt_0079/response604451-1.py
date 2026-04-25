
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize your Telnet connection
tn = telnetlib.Telnet('your_telnet_host')

# Get enabled strings based on configuration
enabled_strings = []
for i in range(1, 4):  # Assuming you have string1, string2, string3
    if config.get('DEFAULT', f'string{i}_enable') == "yes":
        enabled_strings.append(config.get('DEFAULT', f'string{i}'))

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Match found!")
