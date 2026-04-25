
import ConfigParser
import telnetlib

# Load configuration
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Retrieve strings and their enable status
strings = {
    'string1': config.get('Settings', 'string1'),
    'string2': config.get('Settings', 'string2'),
    'string3': config.get('Settings', 'string3')
}

enabled_strings = [key for key, value in strings.items() if config.get('Settings', f'{key}_enable') == 'yes']

# Telnet connection setup
tn = telnetlib.Telnet('hostname')

while True:
    r = tn.read_some()

    if any(x in r for x in enabled_strings):
        # Perform action
        print("Match found, performing action.")
