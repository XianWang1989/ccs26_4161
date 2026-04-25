
import ConfigParser
import telnetlib

# Read configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize enabled strings
enabled_strings = []

# Check which strings are enabled
if config.get('settings', 'string1_enable') == 'yes':
    enabled_strings.append(config.get('settings', 'string1'))
if config.get('settings', 'string2_enable') == 'yes':
    enabled_strings.append(config.get('settings', 'string2'))
if config.get('settings', 'string3_enable') == 'yes':
    enabled_strings.append(config.get('settings', 'string3'))

# Connect to telnet
tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()

    # Check if any enabled string is present
    if any(x in r for x in enabled_strings):
        # Perform action
        print("Matched: ", [x for x in enabled_strings if x in r])
