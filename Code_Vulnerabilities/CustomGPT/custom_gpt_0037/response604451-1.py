
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Retrieve enabled strings
enabled_strings = []
for i in range(1, 4):  # Assuming you have up to 3 strings
    str_key = 'string{}_enable'.format(i)
    if config.get('DEFAULT', str_key) == 'yes':
        str_value = config.get('DEFAULT', 'string{}'.format(i))
        enabled_strings.append(str_value)

# Connect to Telnet
tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Perform your action here
        print("Found a match:", [x for x in enabled_strings if x in r])
