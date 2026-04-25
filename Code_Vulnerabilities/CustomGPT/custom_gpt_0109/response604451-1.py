
import telnetlib
import ConfigParser  # Use 'configparser' for Python 3

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Define the strings based on config
strings = []
for i in range(1, 4):  # Assuming you have string1, string2, string3
    string = config.get('DEFAULT', f'string{i}')
    enabled = config.get('DEFAULT', f'string{i}_enable')
    if enabled.lower() == 'yes':
        strings.append(string)

# Telnet connection and read
tn = telnetlib.Telnet('your.telnet.server')

while True:
    r = tn.read_some()
    if any(x in r for x in strings):
        # Perform the desired action
        print("Match found, performing action...")
