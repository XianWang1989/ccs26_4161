
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize your strings and their enabled states
search_strings = []
for i in range(1, 4):  # Assuming you have three strings
    string_key = 'string{}_enable'.format(i)
    if config.get('DEFAULT', string_key) == 'yes':
        string_value = config.get('DEFAULT', 'string{}'.format(i))
        search_strings.append(string_value)

tn = telnetlib.Telnet('your_telnet_host')

while True:
    r = tn.read_some()

    # Check if any of the enabled strings is in the response
    if any(x in r for x in search_strings):
        # Perform the action
        action()
