import ConfigParser
import telnetlib

# Read configuration file
config = ConfigParser.ConfigParser()
config.read('config.ini')

# Initialize telnet connection
tn = telnetlib.Telnet('your_telnet_server')

# Strings to search for
strings = {
    'string1': 'some_text_1',
    'string2': 'some_text_2',
    'string3': 'some_text_3'
}

# List to hold the strings that are enabled
enabled_strings = []

# Check config file for enabled strings and add to the list
for string_key, string_value in strings.items():
    if config.get('Settings', f'{string_key}_enable') == 'yes':
        enabled_strings.append(string_value)

# Now, use the enabled strings in the search
while True:
    r = tn.read_some()
    if any(x in r for x in enabled_strings):
        # Your action when a match is found
        print("Match found, performing action...")
        break
