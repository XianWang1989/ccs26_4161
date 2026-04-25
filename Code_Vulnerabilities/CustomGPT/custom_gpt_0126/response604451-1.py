
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize the Telnet connection
tn = telnetlib.Telnet('your_telnet_server')

# Strings and their enabling status
strings = {
    'string1': config.get('Settings', 'string1_enable'),
    'string2': config.get('Settings', 'string2_enable'),
    'string3': config.get('Settings', 'string3_enable')
}

# List of strings to check.
search_strings = [key for key, value in strings.items() if value == 'yes']

while True:
    r = tn.read_some()
    if any(x in r for x in search_strings):
        # Perform your action here
        print("Match found!")
